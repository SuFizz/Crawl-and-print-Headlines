import urllib

if __name__ == "__main__":
#	proxy = 'https://:';
#	rt = urllib.urlopen("https://news.ycombinator.com/");
	
	esult = urllib.urlopen("https://news.ycombinator.com/", proxies={'https': proxy})
	

	filelines = esult.readlines();
	
#	t = esult.readline()
	
	req = filelines[21];
	start = 0;
	end = 0;
	si = len(("</span></center></td><td class=\"title\"><a href=\""))
	iss = len(("</a><span class="))

	for i in range(3):
		start = req.index("></span></center></td><td class=\"title\"><a href=\"",start+1);
#		print start,end
		start = start + si;
#		print start,end
#		end = start;
#		print start,end
		end = req.find("</a><span class=",end+1);
#		beg = req[start:].rfind(">")
#		print start, end;
		print req[(req[start:end].index(">"))+1+start:end]
#		end += iss
#		print start,end		

#		if()
	
#	print rt;
