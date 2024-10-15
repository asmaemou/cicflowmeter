from scapy.all import AsyncSniffer
from cicflowmeter.flow_session import generate_session_class

# Create an instance of the modified FlowSession class
NewFlowSession = generate_session_class(output_mode='flow', output_file='', url_model=True)

def test_flow_session():
    # Define an interface (for testing, you can use a test interface or loopback)
    interface = "en0"  # For macOS, 'lo0' is the loopback interface
    
    # Start packet capturing using the modified FlowSession class
    sniffer = AsyncSniffer(iface=interface, session=NewFlowSession, store=False)
    print("Starting the sniffer...")

    try:
        # Start the sniffer and wait for a while to capture some packets
        sniffer.start()
        input("Press Enter to stop capturing packets and send to API...")
    finally:
        sniffer.stop()
        print("Stopped sniffer.")

# Run the test function
if __name__ == "__main__":
    test_flow_session()