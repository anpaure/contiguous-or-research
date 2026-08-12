# External-reserve finish criterion and the K16 two-blocker audit

## General lemma

Let `w` be a word, let `p` be a position, and let `w'` be obtained by changing
only `w[p]`.  For a target mask `t`, write

\[
\mu_{\neg p}^w(t)
  = \#\{[i,j]: \bigvee_{q=i}^j w[q]=t,\ p\notin[i,j]\}.
\]

Suppose `w` has exactly one hole `h` and the edit at `p` installs `h`.  Then
`w'` is universal if and only if every previously covered target whose
`p`-containing witnesses are destroyed by the edit has an external witness,
i.e. a witness counted by `mu_{not p}` which survives the edit.

This is immediate because intervals avoiding `p` are byte-for-byte unchanged;
every changed interval contains `p`.  It is nevertheless the correct search
invariant: ordinary multiplicity can count several witnesses that all contain
the edited position, and therefore supplies no reserve at all.

## K16 specialization

For the authenticated length-12873 one-hole basin
`scratch/rex3_final_fwd_h11373.word` (SHA-256
`b6ed242d0f098f8511d31027b2d485526c5f6482382cd04c6b31ce1d6576b25b`):

- the sole hole is `h = 11373 = 0x2c6d`;
- the 64 minimum-debt edits at position `p=0` all install `h`;
- every such finish deletes the last witnesses of exactly
  `18553 = 0x4879` and `26745 = 0x6879`;
- hence every finished word has exactly those two holes;
- an exhaustive arbitrary one-cell repair after each of the 64 finishes finds
  no universal word.

The annealed basin
`scratch/k16_Hfinal_doubleblocker_h1b3.word` (SHA-256
`445d06607d7074c91be7807769f64d86e6abc5f23a1f999873a09c4d9a42c62f`)
has raw multiplicities

\[
\mu(0x4879)=1,\qquad \mu(0x6879)=2,
\]

but both `0x6879` witnesses contain position 0.  Thus

\[
\mu_{\neg0}(0x4879)=\mu_{\neg0}(0x6879)=0,
\]

and replaying the nominal finish still leaves both holes.  The earlier claim
that raw blocker multiplicity two was finish-ready is therefore retracted.

## Consequence for search

The exact coefficient-one finishing target is not “increase the two blocker
multiplicities.”  It is:

1. retain sole hole `0x2c6d`;
2. create a position-0-avoiding witness of `0x4879`;
3. create a position-0-avoiding witness of `0x6879`;
4. preserve all other targets;
5. apply any authenticated position-0 finish and replay all 65,535 masks.

This external-reserve score is now the appropriate objective for annealing,
exact provider search, and any general seam/reserve lemma.
