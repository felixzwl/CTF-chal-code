f = open('f:/ssctfm200', 'wb')
strr = '9e97ba2a008088c9a370975ba2e499b8c178720f88dddc342b4e7d317fb5e8702269073f5492d9b54a825e91b767e18722e429a4a378b4590511ff88e09ef24265cdd5f97a357dbfe72b1d0dcef6892a7f81ebb82294ec3d637ff6df108768df744ebf8a65456b4e13be55409e0c58270e515d8e6f6169c17337ca4ae1bdb4683fc39b1fb57b9ee1bb329f76190f239a2f95e9b9b27aef766482eeea211b207f17e91b45b08f7ccf8c1273f3df354d310a3a84e869b00598dccfccec9b4c1416720214a6e80e69fe63647f0c8b20e9f331a84b5b93dceb2f4aef1430c253f43a3b4cad178b859912f2119618ef1c59c2685ab9cfe6981b6259ef5a96b51b8de0cd701562c15a29f0248f62a243f77839f0f2c2c9b8451f9e88502199d866c1c502781954f366af0bf162249a95d306cfab48b364ef1dd4cc898787d1424d943a1d2b0d3417d2458aae1b9c13ec6d13110badb81964eb35ce64899292c1b7500c403e0d62b78b2752889164f606387cf0c10dc815d0b9449cebcf7effe84b97e52df102b052bdceae91426c389d834fed52c49f49e78a718996e8571adf94681dedec32357d90e19a0265c05894a5c03717f7cfc8f2a3f621aed1011a7b546c47469f044359ccfb87a520a9a2c93ab0eacce0001018cf180d9a23cd855a733a870192dec0d86e10c802fb76afe6117cdd68067b071abfdfd581766ce462022805d6e602b107bc558b4d5c661844e13914dbb061fc7764047d41d8a5008c7b3fcda84c0415855b525c86ee63d1b00b9c99a0b44cb0362ab27ac4e67bb076e2b87fa459a4e54834f501aaf888ffd9e42fdb425c66f7486defbb446976ee127f541dc259afae4380dc7c60055b03698cce58f39c9fd92045227dc813994ff4cc64d53038ebd71b3b8b8ab4b67ad629a8a89fe2c34ce467543724240f5c2fdd504b766bd6c8734371a44f5bb97c079ba675f3337655b32a0d11d14d22481ba993b7b50189be74c4b17b9107d2bfc0552677891cc701a63037370e5e76e3960a9dcaa0584b7a74a7cd5c59376ef89dd4660c1019e99fa29b5e65ee8efaa3c74a47dbe98d2b5070e99a93e1ec323b219452f9bdedb2164658f7eabb9eeb1733a6421e6ff0fa7bc25aafae3d2eff84717cdb60a12a36e28f86cc53ddf723518fb5460687a73967549219949164c3573a7c17a25e260bdd13f4be781eb9786014f594d4a58db0f1d12e3bab11b8bd41358627856b0d5a990334c38c2ca1a19f2a63ffe00b6d81b0170983d2338fb80915632de59b66e7802324861d4bf39e21c2522ea4e71669c22e2fb7a2d9e2e7236917f77603b216272fb080447e332e839011804876b7e951bbb4b41d1cf797003e587dc1bf56c69ea8c5e47b8baa8a512403494d042a6c877280365ffc44af09d96beb80ed70051fe6477588a71246623ccb0da6644b438ffa040a50b518f6d441dc35fe47596320a440e7407c596320a440e7407c9c913a907da19e7effe3f0a761026d1b21dc7fa90a38d24cc4a1cb76973c048e58c51fe9f05de209019b619716b4a17b2c900fa0469e1574302ebd4e7d0ad43c4a825e91b767e18722e429a4a378b45923e08ce093633b6425e63e19f27ab40816098f0b703078d0ee41c58191322740ba558a54b92a7b4c86ab2900d97b7400733e7ea1d7d43148743ec53dcff09f0148490000b00400006e31396a383c3e3f6c6c313e306a3f30000d1f00'.decode(
    'hex')
f.write(strr)
f.close()

r = open('f:/ssctfm200', 'rb')
f = open('f:/ssctfm200_out', 'wb')
key = 'green'
rs = r.read()
tmp = ''
for i in xrange(len(rs)):
    tmp += chr(ord(rs[i]) ^ ord(key[i % len(key)]))
f.write(tmp)
f.close()
r.close()
