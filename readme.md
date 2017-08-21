# fpasswd



My own command line based password manager.


- the local data file

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

  `fpasswd delete 1`


  ```
  [deleted]1 tabao 遗憾2017 pass8989 2017-01-01-20:00
  ```



## Install

`pip install fpasswd`

or
`pip instal .`


## Contributing

You can publish your password by pull request, thank you.

## Liscense

Just sh1t, eat or not.