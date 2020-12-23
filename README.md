# Shuriken
Web Fuzzer

## Presentation

Shuriken is a web fuzzer that include proxies support and with which you will be able to do some recon : sqli, web discovery, password cracking, ...

## Usage

### Linux :
```sh
Run install .sh : sudo ./install.sh
shuriken -u url -w wordlist [-d] [-p]
```

### Windows :
```sh
pip3 install requests
run shuriken from terminal or wsl
```

## Examples

### Directory Fuzzing : 
```sh
shuriken -u http://mysite/NINJA -w dirlist
```
### Sql injection Discovery : 
```sh
shuriken -u http://mysite/index.php?id=NINJA -w sqlipayloads
```
### Password Cracking : 
```sh
shuriken -u http://mysite/logon.php?user=admin&password=NINJA -w passwords
```

## Media

### Invalid Proxy Detection
![](photo1.PNG)

### Without Proxy
![](photo2.PNG)

### With Proxy
![](photo3.PNG)

### Invalid Syntax
![](photo4.PNG)


## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

