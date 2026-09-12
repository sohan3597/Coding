import math
import struct
import wave
import os

def generate_sine_wave(frequency=1000.0, amplitude=1.0, duration=1.0, sample_rate=44100):
    """
    Generates a sine wave of a given frequency, amplitude, duration, and sample rate.
    
    Args:
        frequency (float): Frequency of the sine wave in Hz (default: 1000 Hz).
        amplitude (float): Unit amplitude (default: 1.0).
        duration (float): Duration of the wave in seconds (default: 1.0 s).
        sample_rate (int): Number of samples per second (default: 44100 Hz).
        
    Returns:
        list of tuples: A list containing (time, value) pairs.
    """
    num_samples = int(sample_rate * duration)
    samples = []
    
    for i in range(num_samples):
        # Time in seconds
        t = i / sample_rate
        # Sine wave formula: y(t) = A * sin(2 * pi * f * t)
        val = amplitude * math.sin(2 * math.pi * frequency * t)
        samples.append((t, val))
        
    return samples

def save_as_csv(samples, filename="sine_wave_1khz.csv"):
    """
    Saves the generated wave samples to a CSV file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("Time (s),Amplitude\n")
            for t, val in samples:
                f.write(f"{t:.8f},{val:.8f}\n")
        print(f"Successfully saved samples to CSV: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_as_wav(samples, filename="sine_wave_1khz.wav", sample_rate=44100):
    """
    Saves the generated wave samples to a 16-bit mono WAV file.
    """
    num_channels = 1  # Mono
    sampwidth = 2      # 2 bytes = 16 bits
    
    try:
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(num_channels)
            wav_file.setsampwidth(sampwidth)
            wav_file.setframerate(sample_rate)
            
            for _, val in samples:
                # Scale from [-1.0, 1.0] to 16-bit signed integer range [-32767, 32767]
                # Clip to prevent overflow if amplitude is slightly larger than 1.0
                clamped_val = max(-1.0, min(1.0, val))
                int_val = int(clamped_val * 32767)
                # Pack as 16-bit signed integer ('h' format in struct)
                data = struct.pack('<h', int_val)
                wav_file.writeframesraw(data)
                
        print(f"Successfully saved audio to WAV: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error saving to WAV: {e}")

def plot_samples(samples, frequency=1000.0, num_cycles_to_show=5):
    """
    Attempts to plot the first few cycles of the sine wave using matplotlib.
    If matplotlib is not installed, prints a text-based plot in the console.
    """
    # Calculate duration of the number of cycles we want to show
    # Period T = 1 / f
    period = 1.0 / frequency
    display_duration = period * num_cycles_to_show
    
    # Filter samples within the display duration
    plot_data = [(t, val) for t, val in samples if t <= display_duration]
    
    try:
        import matplotlib.pyplot as plt
        
        times = [t * 1000 for t, val in plot_data]  # Convert to milliseconds
        amplitudes = [val for t, val in plot_data]
        
        plt.figure(figsize=(10, 4))
        plt.plot(times, amplitudes, label=f'{frequency/1000:.1f} kHz Sine Wave', color='blue', linewidth=2)
        plt.title(f'Sine Wave ({frequency/1000:.1f} kHz, Unit Amplitude)')
        plt.xlabel('Time (ms)')
        plt.ylabel('Amplitude')
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.ylim(-1.2, 1.2)
        plt.legend()
        
        plot_filename = "sine_wave_1khz_plot.png"
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Successfully saved plot to image: {os.path.abspath(plot_filename)}")
        
    except ImportError:
        print("\nmatplotlib is not installed; skipped generating PNG plot.")
        print("Here is a brief text visualization of the first cycle:")
        # Show text-based visualization of the first cycle
        one_cycle_samples = [val for t, val in plot_data if t <= period]
        # Downsample for visualization
        step = max(1, len(one_cycle_samples) // 20)
        for val in one_cycle_samples[::step]:
            width = int((val + 1.0) * 20)  # scale to 0-40 characters
            print(" " * width + "*")

if __name__ == "__main__":
    print("Generating 1 kHz Sine Wave with unit amplitude...")
    
    # Parameters
    frequency = 1000.0   # 1 kHz
    amplitude = 1.0      # Unit amplitude
    duration = 1.0       # 1 second duration
    sample_rate = 44100  # CD Quality
    
    # Generate samples
    samples = generate_sine_wave(frequency, amplitude, duration, sample_rate)
    
    # Print statistics/first few samples
    print(f"Generated {len(samples)} samples at {sample_rate} Hz.")
    print("First 5 samples:")
    for i in range(min(5, len(samples))):
        t, val = samples[i]
        print(f"  t = {t:.6f} s, amplitude = {val:.6f}")
        
    # Save options
    save_as_csv(samples, "sine_wave_1khz.csv")
    save_as_wav(samples, "sine_wave_1khz.wav", sample_rate)
    
    # Try to plot
    plot_samples(samples, frequency, num_cycles_to_show=5)