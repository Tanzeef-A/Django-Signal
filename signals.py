from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Define a receiver
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver executed")