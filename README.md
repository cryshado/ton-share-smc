### ton-share-smc

![FunC](https://img.shields.io/badge/made%20with-FunC-brightgreen)
![Fift](https://img.shields.io/badge/made%20with-Fift-brightgreen)
![TON](https://img.shields.io/badge/based%20on-The%20Open%20Network-blue)

Allows incoming transactions to be divided into two parts. Can be useful, for example, 
when you want to share profits with your partner. During initialization the share
in percent of each of the two partners is set.

#### Build

```bash
func -SPA -o auto/simple-share-code.fif lib/stdlib.fc simple-share.fc
```

#### LICENSE

All source code, except the files in the `lib` directory, is distributed under the the `GPL-3.0 License`. The licenses of the libraries that are in the `lib` folder are listed at the head of the each library file.