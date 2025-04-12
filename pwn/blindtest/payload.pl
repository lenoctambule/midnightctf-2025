use strict;
use warnings;
use constant SYS_writev => 20;
open my $fh, "<", "./flag.txt" or die "Cant open file $!";
my $file_content = do {local $/; <$fh>};
my @buffers = ($file_content, "\n");
my $iovec = pack("L!L!L!L!L!L!",
    map { 
        my $str = $_;
        my $ptr = unpack("L!", pack("P", $str));
        my $len = length($str);
        ($ptr, $len)
    } @buffers
);
my $fd = fileno(STDOUT);
my $ret = syscall(SYS_writev, $fd, $iovec, scalar(@buffers));
