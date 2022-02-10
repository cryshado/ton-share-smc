### ton-share-smc

Allows incoming transactions to be divided into two parts. Can be useful, for example, when you want to share profits with your partner. During initialization the share in percent of each of the two partners is set.

#### Build

```bash
func -SPA -o auto/simple-share-code.fif lib/stdlib.fc simple-share.fc
```

#### LICENSE

All source code except the files in the `lib` directory is under the `GNU General Public License v3.0`. The licenses of the libraries that are in the `lib` folder are listed at the head of the each library file.