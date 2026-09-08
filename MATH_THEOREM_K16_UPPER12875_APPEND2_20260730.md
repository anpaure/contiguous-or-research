# A verified two-cell completion at k=16

Let `P` be the authenticated length-12,873 partial word
`scratch/k16_12873_repaired_partial.word`.  Its exhaustive coverage defect is
exactly

\[
\{0x287d,\;0xce61,\;0xce63\}.
\]

Append the two masks

\[
x=0x0200,\qquad y=0x287d.
\]

Appending cannot destroy any interval already present in `P`.  The three old
holes acquire the following literal witnesses (indices are zero based in the
new word):

\[
\begin{aligned}
0x287d &= y && [12874,12874],\\
0xce61 &= 0xcc61\lor x && [12871,12873],\\
0xce63 &= 0xcc63\lor x && [12870,12873].
\end{aligned}
\]

Thus `P,x,y` is universal and has length 12,875.  A standalone C++ replay and
the repository verifier independently check all 65,535 nonempty masks.  The
certificate is `answers/k16_upper12875.word`, SHA-256
`d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9`.

Together with the proved counting bound, the current exact bracket is

\[
\boxed{12873\le \nu(16)\le12875.}
\]

This does not prove optimality.  It improves the previous verified upper bound
12,876 by one and leaves a gap of two.
