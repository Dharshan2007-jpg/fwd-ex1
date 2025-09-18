from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
 <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TCP/IP Protocol Table</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f4f9;
      margin: 20px;
    }
    h2 {
      text-align: center;
    }
    table {
      border-collapse: collapse;
      width: 80%;
      margin: auto;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      background: #fff;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 12px;
      text-align: center;
    }
    th {
      background: #0077b6;
      color: white;
    }
    tr:nth-child(even) {
      background: #f9f9f9;
    }
    tr:hover {
      background: #e6f7ff;
    }
  </style>
</head>
<body>

  <h2>TCP/IP Protocol Layers</h2>

  <table>
    <tr>
      <th>Layer</th>
      <th>Protocols</th>
      <th>Functions</th>
    </tr>
    <tr>
      <td>Application</td>
      <td>HTTP, FTP, SMTP, DNS</td>
      <td>Provides services for end-user applications</td>
    </tr>
    <tr>
      <td>Transport</td>
      <td>TCP, UDP</td>
      <td>End-to-end communication, reliability, error checking</td>
    </tr>
    <tr>
      <td>Internet</td>
      <td>IP (IPv4, IPv6), ICMP</td>
      <td>Logical addressing and routing of packets</td>
    </tr>
    <tr>
      <td>Network Access (Link)</td>
      <td>Ethernet, Wi-Fi, ARP</td>
      <td>Defines physical addressing and access to media</td>
    </tr>
  </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()