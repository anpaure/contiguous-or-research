# Economical queue covers through every `o(sqrt(log m))` depth

## Verdict

The dummy-completed queue hypergraph should be rounded by an economical
**cover**, not necessarily by a matching.  This removes the requirement that
the matching leave only `o(W)` vertices among a band of order `hW` vertices.

Put

\[
 W=\binom{2m}{m},\qquad L=\log m.
\]

For every integer function

\[
 1\le h=o(\sqrt L),
\]

there is a literal nonzero OR word covering every mask in the ranks
`m-h,...,m+h` and having length `(1+o(1))W`.  The simple choice

\[
 H=\lceil\sqrt L\rceil
\tag{0.1}
\]

already proves this.  More quantitatively, its length is at most

\[
 W\left[
  1+O\left(
    \frac{h+1}{\sqrt L}
    +\exp\left\{-(1+o(1))\frac{\sqrt L}{2h+1}\right\}
  \right)
 \right].
\tag{0.2}
\]

The selected atoms may overlap.  The overlap is harmless: an economical
edge cover controls the number of selected atoms directly, and the exact
ledger below shows that its middle duplicates are only the cover-size
excess.

This is a quantitative improvement for the structured queue/MTF route.  It
does **not** improve the largest known raw OR-covered depth, because the
cyclic-strip construction already covers every `J=o(sqrt(log m))`.  It also
does not reach the moderate-deviation tail depth and therefore does not prove
the coefficient-one theorem.

## 1. Exact missing--duplicate--total ledger

For a selected family of `p` queue atoms, and for each real signed band row
`r`, write

\[
 \mu_r(S)=\#\{\hbox{selected atoms containing }S\},
\]

and define

\[
 \begin{split}
 M_r&=\#\{S:\mu_r(S)=0\},\\
 D_r&=\sum_S(\mu_r(S)-1)_+,\\
 T_r&=\sum_S\mu_r(S).
 \end{split}
\]

If the row has `N_r` masks, then exactly

\[
 \boxed{M_r=N_r+D_r-T_r.}
\tag{1.1}
\]

Indeed, `T_r=(N_r-M_r)+D_r`.

Every atom contains exactly `H` middle masks and has a literal word of length
at most `H+2h+1`.  Hence `T_0=pH`, where `N_0=W`.  Concatenating all atom
words and then appending every missing real band mask gives

\[
 \begin{split}
 \mathcal L
 &\le p(H+2h+1)+\sum_r M_r\\
 &=\boxed{W+D_0+(2h+1)p+\sum_{r\ne0}M_r.}
 \end{split}
\tag{1.2}
\]

Thus nonmiddle duplicate counts are not charged directly.  They matter only
if they produce missing masks.  A full augmented edge cover has `M_r=0` in
every real row, and then

\[
 D_0=pH-W.
\tag{1.3}
\]

Consequently a cover using `(1+o(1))W/H` atoms gives both `D_0=o(W)` and a
word of length `W+o(W)` whenever `h/H=o(1)`.

## 2. Dummy-completed fractional hypergraph

Use the monotone-profile queue atoms with `H+h<=m`.  At unsigned depth `q`,
put

\[
 N_q=\binom{2m}{m-q},\qquad \rho_q=N_q/W,
\]

and, for a common uniform `U in [0,1)`, set

\[
 a_q=\lfloor H\rho_q+U\rfloor.
\]

The common `U` makes the `a_q` nonincreasing.  Exactly `a_q` queue starts are
real at each of the two signed depth-`q` rows.  Complete the other `H-a_q`
slots by an independent uniform injection into a row-specific dummy set of
size `W-N_q`.  The middle row has no dummies.  Dummy sets and injections for
different signed rows are independent.

Every augmented edge then has size

\[
 K=H(2h+1)
\tag{2.1}
\]

on a universe of size

\[
 |V|=(2h+1)W.
\tag{2.2}
\]

Every real and dummy vertex has inclusion probability exactly `H/W`.
Therefore, after aggregating equal augmented supports,

\[
 x_e=(W/H)\Pr(E=e)
\tag{2.3}
\]

is an exact fractional perfect matching (and hence an exact fractional edge
cover) of total mass `W/H`.

The weighted pair-codegree satisfies

\[
 \max_{u\ne v}\sum_{e\supseteq\{u,v\}}x_e
 \le \frac{H}{m-h}.
\tag{2.4}
\]

For two real masks this follows by conditioning on the unique queue slot of
the first mask.  The second mask has at most `H` eligible slots, and each
compatible fixed slot has stabilizer-orbit probability at most `1/(m-h)`.
The only distinct nontrivial denominator-one case would be complementary
position intervals; it is impossible because all active intervals omit the
last queue coordinate.  Real--dummy and dummy--dummy codegrees are
exponentially smaller, using

\[
 W-N_1=W/(m+1),
\]

and the independence of the dummy injections.

## 3. Simple Bernoulli support sparsification

It is unnecessary to invoke a multihypergraph version of the matching or
covering theorem.  An augmented support determines the unordered family of
its `H` middle windows.  Those windows induce a Johnson path, so their order
is determined up to reversal.  Conditional on its first middle set, there
are exactly

\[
 (m)_{H-1}^2
\]

ordered geodesic queue paths.  Hence every distinct augmented support obeys

\[
 \Pr(E=e)\le \frac{2}{W(m)_{H-1}^2},
 \qquad
 x_e\le \frac{2}{H(m)_{H-1}^2}.
\tag{3.1}
\]

Take `Lambda=m^8`.  Since `H=o(m)` and `H->infinity`,

\[
 \max_e \Lambda x_e=o(1).
\]

Retain each **distinct support edge** independently with probability
`Lambda x_e`.  This produces a simple `K`-uniform hypergraph.  Every vertex
has expected degree `Lambda`, while every pair has expected codegree at most

\[
 \mu_*\le \Lambda H/(m-h).
\]

Bernoulli Chernoff bounds and union bounds over the `exp(O(m))` vertices and
pairs yield a deterministic realization with

\[
 d(v)=\Lambda+O(\sqrt{\Lambda m})
\tag{3.2}
\]

for every vertex and

\[
 C:=\Delta_2\le 2\Lambda H/(m-h)+1.
\tag{3.3}
\]

## 4. ABKV economical-cover theorem

Use Theorem 3.7 of Alon--Bollobas--Kim--Vu, *Economical covers with
geometric applications*.  Its near-regular hypothesis is satisfied.  With
`D=Lambda+O(sqrt(Lambda m))`, the degree spread in (3.2) is

\[
 o\left((D^2C\log D)^{1/3}\right).
\]

For the choice (0.1),

\[
 K=H(2h+1)=o(L).
\]

Furthermore,

\[
 \log\frac{e^{2K}C\log D}{D}
 =-L+2K+O(\log L)\longrightarrow-\infty.
\tag{4.1}
\]

Thus ABKV gives an edge cover of size

\[
 p\le\frac{|V|}{K}(1+O(\eta))
   =\frac WH(1+O(\eta)),
\tag{4.2}
\]

where

\[
 \begin{split}
 \eta
 &=\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}\\
 &\le\left(O\left(\frac{H\log m}{m}\right)\right)^{1/(K-1)}\\
 &=\exp\left\{-(1+o(1))\frac{\sqrt L}{2h+1}\right\}
 =o(1).
 \end{split}
\tag{4.3}
\]

The cover includes all dummy vertices, which is stronger than needed, but it
also includes every real band mask.  Discard the dummy labels and concatenate
the actual queue words associated with the selected edges.  Combining
(4.2)--(4.3) gives

\[
 \begin{split}
 \mathcal L
 &\le p(H+2h+1)\\
 &\le W(1+O(\eta))
       \left(1+\frac{2h+1}{H}\right),
 \end{split}
\tag{4.4}
\]

which is precisely (0.2).

## 5. Scope and architecture ceiling

This argument proves a genuine queue/MTF cover through every

\[
 h=o(\sqrt{\log m}).
\]

It removes the earlier `sqrt(log log m)` denominator caused by demanding an
augmented matching with only `o(W)` uncovered vertices.  An economical cover
has no holes, and only its relative edge-count excess must tend to zero.

There is also a natural ceiling for this particular black-box architecture.
Any queue-atom scheme with `o(W)` middle repair has

\[
 pH\ge W-o(W).
\]

Its reset contribution is consequently at least order `hW/H`, so leading
constant one requires `H/h->infinity`.  Therefore

\[
 K=H(2h+1)\gg h^2.
\]

Aligned adjacent-depth mask pairs in the queue distribution have normalized
codegree `Theta(1/m)`.  In the ABKV cover estimate this makes `eta->0` require
`K=o(log m)`.  Combining these two requirements gives

\[
 h=o(\sqrt{\log m}).
\]

This is a ceiling of the generic sparsified-ABKV queue-cover method, not a
proof that specially correlated queue covers cannot go deeper.

Finally, the cyclic-strip economical cover already reaches every
`J=o(sqrt(log m))` as a raw literal OR word.  The new result matches that
depth scale while retaining the more rigid monotone-profile queue/MTF atom
structure.  The outer tail still requires depth of order
`sqrt(m log log m)`, so no constant-one construction follows from this
central-band theorem alone.
