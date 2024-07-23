/**
 * A stoppable timer service that executes a callback function at a specified interval.
 */
class StoppableTimerService {
  private timespan: number;
  private callback: () => void | Promise<void>;
  private cancellation: CancellationTokenSource;
  private intervalId: number | null = null;

  /**
   * Constructs a new instance of the StoppableTimerService class.
   * @param timespan The interval at which the callback function is executed.
   * @param callback The callback function to execute.
   */
  constructor(timespan: number, callback: () => void | Promise<void>) {
      if (timespan <= 0) {
          throw new Error('Timespan must be a positive number');
      }
      if (typeof callback !== 'function') {
          throw new Error('Callback must be a function');
      }
      this.timespan = timespan;
      this.callback = callback;
      this.cancellation = new CancellationTokenSource();
  }

  /**
   * Starts the timer.
   */
  public start(): void {
      const cts = this.cancellation; // safe copy
      this.intervalId = setInterval(() => {
          try {
              if (cts.token.isCancellationRequested) return;
              this.callback();
          } catch (error) {
              // Handle the error
              throw error; // Re-throw the error
          }
      }, this.timespan);
  }

  /**
   * Stops the timer.
   */
  public stop(): void {
      if (this.intervalId !== null) {
          clearInterval(this.intervalId);
          this.intervalId = null;
      }
      this.cancellation.cancel();
      this.cancellation = new CancellationTokenSource();
  }

  /**
   * Disposes of any resources held by the timer.
   */
  public dispose(): void {
      // Dispose logic goes here if needed
  }
}
