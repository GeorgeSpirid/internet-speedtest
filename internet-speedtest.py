import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    
    print("Finding the best server...")
    st.get_best_server()
    
    print("Performing download test...")
    download_speed = st.download()
    
    print("Performing upload test...")
    upload_speed = st.upload()
    
    ping_result = st.results.ping
    
    print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping_result:.2f} ms")

if __name__ == "__main__":
    test_internet_speed()