# An exact all-depth \(2^d\)-top placeholder cube exchange

Date: 2026-07-26

Scope: constant-one promotion coupling. This is a higher-dimensional
extension of the audited four-top quartet. It is an exact legal
load-preserving exchange, not a balancing theorem.

## 0. The theorem

Let \(\Omega\) be an \(N\)-set, let \(M<N\), and choose an integer

\[
2\le d\le \min\{M,N-M\}.                                      \tag{0.1}
\]

Choose an \((M-d)\)-set \(C\), disjoint pairs

\[
\{a_{j,0},a_{j,1}\}\qquad(1\le j\le d),
\]

all disjoint from \(C\), and put

\[
U_\epsilon=C\cup\{a_{j,\epsilon_j}:1\le j\le d\},
\qquad \epsilon\in\{0,1\}^d.                                  \tag{0.2}
\]

The two bounds in (0.1) are exactly what is needed: \(d\le M\) makes
the common \((M-d)\)-set meaningful, and \(d\le N-M\) lets the
\(M+d\) labels in (0.2) fit in \(\Omega\).

Fix a cyclic positional word \(\omega\) on

\[
C\cup\{P_1,\ldots,P_d\}.
\]

Let \(\sigma,\tau\in S_d\). Form two positional words
\(\omega^\sigma,\omega^\tau\) by permuting only the placeholder symbols
among their \(d\) fixed placeholder positions; every label of \(C\)
stays in its original position. On top \(U_\epsilon\), substitute
\(a_{j,\epsilon_j}\) for \(P_j\), obtaining actual cyclic frames
\(\pi_\epsilon^\sigma,\pi_\epsilon^\tau\).

For a phase \(s\) and an interval length \(1\le\ell<M\), let

\[
v_\epsilon^\rho(s,\ell)
 =e_{I_{\pi_\epsilon^\rho}(s,\ell)}
\qquad(\rho\in\{\sigma,\tau\})                                  \tag{0.3}
\]

be the corresponding global interval basis vector.

### Theorem 0.1 (higher placeholder cube)

For every phase and every proper interval length,

\[
\boxed{
\sum_{\epsilon\in\{0,1\}^d}(-1)^{|\epsilon|}
\left(v_\epsilon^\sigma(s,\ell)
      -v_\epsilon^\tau(s,\ell)\right)=0.}                       \tag{0.4}
\]

Consequently the compound replacement

\[
\begin{cases}
\pi_\epsilon^\sigma\longleftrightarrow\pi_\epsilon^\tau,
   &|\epsilon|\ \text{even},\\
\pi_\epsilon^\tau\longleftrightarrow\pi_\epsilon^\sigma,
   &|\epsilon|\ \text{odd},
\end{cases}                                                     \tag{0.5}
\]

preserves every phase-tagged interval load at every length
simultaneously, provided the retained phase set or phase-to-tag schedule
is common to every cube corner and to both placeholder permutations. It
therefore preserves all middle ownership, every signed entrance load,
all such common stopping-tag censuses, and any real weighted sum of
positional phase columns. Corner-dependent tag schedules are not covered
by the identity.

For the critical promotion parameters

\[
N=2m,\qquad M=m+H,
\]

the allowed range is

\[
2\le d\le m-H.                                                   \tag{0.6}
\]

This is the full possible Johnson-distance range between two
\(M\)-tops: any two such tops have intersection at least \(2H\), and
\(M-2H=m-H\).

## 1. Proof of the column identity

Fix \(s,\ell\), and inspect the positional interval in
\(\omega^\rho\), where \(\rho\in\{\sigma,\tau\}\).
Let \(J_\rho\subseteq[d]\) be the indices of the placeholders contained
in this interval, and let \(B\subseteq C\) be the contained ordinary
labels. The set \(B\) is independent of \(\rho\), because the
placeholder permutations do not move any ordinary label.

After substitution, the interval set is

\[
B\cup\{a_{j,\epsilon_j}:j\in J_\rho\}.                           \tag{1.1}
\]

First suppose \(J_\rho\ne[d]\). Choose
\(h\in[d]\setminus J_\rho\). The vector in (1.1) is independent of
\(\epsilon_h\), while the signs of the two choices of \(\epsilon_h\)
are opposite. Hence

\[
\sum_\epsilon(-1)^{|\epsilon|}
v_\epsilon^\rho(s,\ell)=0.                                     \tag{1.2}
\]

Now suppose \(J_\rho=[d]\). Then the interval set is

\[
B\cup\{a_{1,\epsilon_1},\ldots,a_{d,\epsilon_d}\},              \tag{1.3}
\]

which depends on \(\epsilon\) but not on the permutation \(\rho\).
Thus, if both \(J_\sigma=J_\tau=[d]\), the two alternating sums are
identical.

It remains only to note that

\[
J_\sigma=[d]\quad\Longleftrightarrow\quad J_\tau=[d],            \tag{1.4}
\]

because \(\sigma,\tau\) merely permute the \(d\) placeholder symbols
among the same \(d\) positional slots. Therefore either both
alternating sums vanish by (1.2), or they coincide termwise by (1.3).
This proves (0.4). \(\square\)

The two excluded lengths are harmless.  At length zero every interval is
empty, while at length \(M\) the interval is the whole top
\(U_\epsilon\), independently of \(\rho\).  Hence the old--new
difference vanishes corner by corner at both boundary lengths.  In
particular, the exchange also preserves the upper-boundary top load.

## 2. Exact scope

The theorem supplies a legal exchange at every common-core distance,
but it has two costs.

1. A distance-\(d\) move uses all \(2^d\) corners of a top cube.
2. It is load-neutral. It changes positional chronology while leaving
   every audited load fixed.

Thus it can serve as a nonabelian connectivity generator after a good
load table has been found. It cannot by itself decrease the floor
energy or create missing target coverage.

Compared with quartets, the higher cube removes one specific physical
barrier: four tops need not share an \((M-2)\)-template when a larger
common core is available. A \(d\)-cube needs only a common
\((M-d)\)-template and permits an arbitrary permutation of its \(d\)
placeholder labels. Whether a coefficient-one construction contains
enough such complete cubes, and whether their nonnegative moves connect
the joint common-permutation fibre with only \(o(W)\) exceptions, remain
open.
