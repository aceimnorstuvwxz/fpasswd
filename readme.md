# fpasswd



My own command line based password manager.



- show help

  `fpasswd`


- set up the local file to save data

  `fpasswd config —path "~/.fpasswd" `

  pure lightwight, no encryption exist, just plain text

  the default location is `~/.fpasswd`

- add password line

  `fpasswd add taobao 遗憾2017 pass8989`

- find with keyword

  `fpasswd find taobao`

  ```
  1 tabao 遗憾2017 pass8989 2017-01-01-20:00
  3 tabao2 战胜2 时的飞机 2017-2-2 30:00
  ```

- delete certain one 

  `fpasswd remove 1`


  ```
  [removed]1 tabao 遗憾2017 pass8989 2017-01-01-20:00
  ```



## Install

`pip install fpasswd`



## Liscense

I'm glad if you need this piece of thit, so do what ever you want with it with no warrant provided.

MIT 9.0



Powered by Tencent 7.0 Nxe999xx

M4j0r