#!/usr/bin/perl
use CGI;
main();

sub main {
	my $file = CGI::param("file");
	my $type = CGI::param("type");
	my $test = CGI::param("test");
	if ($file =~ /\.\// or $file =~ /flag/ or $file =~ /\//) {
		print CGI::header(-type=>"text/html", -status=> '403 forbidden');
		exit;
	}
	if($test) {
		if (!open(TST, "<$test")) {
			print CGI::header(-type=>"text/html", -status=> '404 not found');
			exit;
		}
	}
	if($type eq "css"){
		print "Content-type: text/css\n\n";
	}
	elsif($type eq "html"){
		print "Content-type: text/html\n\n";
	}
	elsif($type eq "javascript"){
		print "Content-type: text/javascript\n\n";
	}
	open (FH, "<$file");
	print while (<FH>);
	close (FH);
	exit(0);
}
