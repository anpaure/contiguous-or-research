# Fifth-wave D: multiframe SCD surgery and telescoping reset tolls

Date: 2026-07-25

## 1. Verdict

This route does not yet prove the contiguous-OR width conjecture or
\(\mathrm{RSCD}_A\). It does, however, prove that the corrected exact
hard-reset toll \(2d\) genuinely telescopes under time-dependent radius
changes, and it supplies an unconditional multiframe saving inside one exact
full SCD.

There are six theorem-level advances.

1. A nonincreasing queue of radii
   \(d_0\ge d_1\ge\cdots\ge d_{\ell-1}\) exposes \(\ell\) pairwise-disjoint
   symmetric chains in a literal word of length exactly
   \(\ell+2d_0\). Independently resetting its constant-radius pieces would
   pay \(2\sum r_j\); the shared word pays only \(2r_1\).
2. For every exact band SCD resolved into such atoms, the reset ledger has
   the exact Ferrers-capacity lower bound
   \[
   \widehat{\mathfrak R}
   =2\sum_{q=1}^h A_q
   \ge2\sum_{q=1}^h\left\lceil\frac{N_q}{L}\right\rceil,
   \]
   where \(L\) is the maximum atom length and \(A_q\) counts atoms reaching
   depth \(q\). The bound is attained by an integral profile table and by an
   exact fractional coordinate-orbit cover. For
   \(h=A\sqrt m\), \(L=m-h\), its value is
   \[
   \left(\sqrt\pi\,\operatorname{erf}(A)+o(1)\right)
   \frac{W}{\sqrt m}=o(W).
   \]
   Thus local reset accounting is not the asymptotic obstruction; integral
   mask-disjoint resolution is.
3. In the standard product SCD of a positive, nonterminal radius-\(d\)
   parent chain with \(B_2\), the four child chains of radii
   \(d+1,d,d,d-1\) admit one literal multiframe tour with exact prefix
   overhead \(4d+1\), versus \(8d\) for four independent starts. Together
   with separate zero-radius and terminal treatments, this works inside one
   genuine full SCD color class.
4. A recency-inversion lemma proves that the \(2d\)-step switch between the
   two radius-\(d\) product frames is optimal. Monotone radius loss can
   telescope, but moving a marker through a depth-\(d\) singleton queue
   cannot.
5. Every exact queue-resolved band SCD produces a two-sided-rainbow linear
   forest at depth one. If \(\Lambda_m\) is the largest possible size of
   such a forest, then
   \[
   \widehat{\mathfrak R}\ge2(N_1-\Lambda_m).
   \]
   More generally, relative to an allowed edge reservoir \(E\),
   \[
   \widehat{\mathfrak R}+2s
   \ge2(N_1-\lambda(E)),
   \]
   where \(s\) is the number of internal transitions outside \(E\). For the
   Greene--Kleitman projection reservoir, the corrected plane-tree DP gives
   \(\lambda(E)=m\operatorname{Cat}_m-\Delta_m=N_1-\Delta_m\), and hence the
   exact robust obstruction
   \[
   \widehat{\mathfrak R}+2s\ge2\Delta_m
   =(0.713791735784\ldots+o(1))W.
   \]
6. Time dependence cannot be compressed into a small fixed library of
   coordinate frames. If a queue resolution uses only \(K\) perfect-matching
   frames, then
   \[
   \widehat{\mathfrak R}
   \ge 2\sum_{q>K/2}\left\lceil\frac{N_q}{K}\right\rceil.
   \]
   Hence an \(o(W)\)-reset resolution on the window
   \(h=A\sqrt m\) requires at least
   \((2A-o(1))\sqrt m\) distinct frames. This is a genuine multiframe
   invariant: arbitrary alternation among fewer frames does not evade it.

The third result is the requested exact-SCD special case beyond fixed
radii. The second, fifth, and sixth results are new invariant lower bounds.
None is silently promoted to an asymptotic integral SCD construction.

Throughout,

\[
W=\binom{2m}{m},
\qquad
N_q=\binom{2m}{m-q},
\qquad
\operatorname{Cat}_m=\frac{W}{m+1}.
\tag{1.1}
\]

All exact-prefix formulas exclude the terminal radius \(d=m\). The fixed
windows considered below satisfy this automatically for large \(m\).

## 2. Exact monotone-radius telescoping

Let \(0\le h<m\), let \(1\le\ell\le m-h\), and choose distinct
coordinates

\[
z_{-h},z_{-h+1},\ldots,z_{\ell+m-2}
\tag{2.1}
\]

from a \(2m\)-element ground set. For \(0\le t<\ell\), put

\[
S_t=\{z_t,z_{t+1},\ldots,z_{t+m-1}\}.
\tag{2.2}
\]

For \(0\le d\le h\), define the radius-\(d\) symmetric chain centered at
\(S_t\) by its rank-\((m+s)\) member

\[
C_t^s(d)=\{z_{t-s},z_{t-s+1},\ldots,z_{t+m-1}\},
\qquad -d\le s\le d.
\tag{2.3}
\]

Its lower endpoint is

\[
L_t^{(d)}=C_t^{-d}(d)
=\{z_{t+d},\ldots,z_{t+m-1}\}.
\tag{2.4}
\]

Let

\[
d_0\ge d_1\ge\cdots\ge d_{\ell-1}
\tag{2.5}
\]

be a nonincreasing radius profile.

### Theorem 2.1 (literal multiframe queue atom)

Write the \(2d_0+1\) initial entries

\[
\{z_{-d_0}\},\{z_{-d_0+1}\},\ldots,
\{z_{d_0-1}\},L_0^{(d_0)},
\tag{2.6}
\]

and then append

\[
L_t^{(d_t)}\qquad(1\le t<\ell).
\tag{2.7}
\]

The resulting literal word has length

\[
\boxed{\ell+2d_0}
\tag{2.8}
\]

and exposes the complete chain \(C_t(d_t)\) by contiguous suffix ORs at its
\(t\)-th designated endpoint. All exposed masks are distinct.

### Proof

At time zero the last-occurrence partition begins

\[
L_0^{(d_0)},
\{z_{d_0-1}\},\ldots,\{z_{-d_0}\}.
\tag{2.9}
\]

Its first \(2d_0+1\) prefix unions are exactly (2.3). Coordinates not yet
written may be regarded as one virtual oldest tail; they do not belong to
any required prefix union.

Inductively suppose that at time \(t\) the state begins

\[
L_t^{(d)},
\{z_{t+d-1}\},\ldots,\{z_{t-d}\},
\tag{2.10}
\]

where \(d=d_t\). Put \(e=d_{t+1}\le d\) and append

\[
X=L_{t+1}^{(e)}
=\{z_{t+e+1},\ldots,z_{t+m}\}.
\tag{2.11}
\]

If \(e<d\), the update by \(X\) absorbs the old lower block and all leading
singletons through \(z_{t+e+1}\). The new state begins

\[
X,\{z_{t+e}\},\ldots,\{z_{t+1-e}\}.
\tag{2.12}
\]

If \(e=d\), then

\[
L_t^{(d)}\setminus X=\{z_{t+d}\},
\]

so (2.12) holds again. Old singleton fragments and the unseen residual stay
after the displayed prefix. They need not merge into one compact residual
block and cannot affect the desired suffix ORs. This proves the literal
induction.

For fixed rank \(m+s\), (2.3) is a nonempty proper interval in the injective
linear queue. Changing \(t\) deletes one endpoint and adds another, so two
different times cannot give the same mask. Masks at different ranks have
different sizes. Thus the chains are pairwise disjoint. The entry count in
(2.8) is immediate from (2.6)--(2.7). \(\square\)

### Corollary 2.2 (exact reset telescoping)

Suppose the profile has maximal constant-radius runs at the distinct radii

\[
r_1>r_2>\cdots>r_s.
\]

These pieces are ordinary same-radius rotor runs. Giving them separate exact
hard resets produces length

\[
\ell+2\sum_{j=1}^sr_j.
\tag{2.13}
\]

The shared multiframe word has length \(\ell+2r_1\), and therefore saves
exactly

\[
\boxed{2\sum_{j=2}^sr_j.}
\tag{2.14}
\]

The seams at which the radius drops are one-entry MTF prefix transitions,
not rotor arcs. Hence (2.14) does not contradict the radiuswise no-averaging
theorem for the rotor master.

Writing the complete residual block before (2.6) adds one entry. Thus the
conservative complete-state word has length \(\ell+2d_0+1\); the exact
prefix-extraction word is (2.8).

## 3. The exact Ferrers reset invariant

Fix a band of depths \(0\le q\le h\). A saturated SCD of that band has
exactly \(W\) chain centers, and exactly

\[
N_q=\binom{2m}{m-q}
\tag{3.1}
\]

of its chains reach depth \(q\). Suppose its chains are partitioned into
monotone queue atoms as in Theorem 2.1, each with at most \(L\) centers.

For atom \(i\), let \(\ell_i\le L\) be its length, let
\(d_{i,0}\) be its initial and maximum radius, and let

\[
a_{i,q}=|\{t:d_{i,t}\ge q\}|.
\tag{3.2}
\]

Then

\[
\ell_i=a_{i,0}\ge a_{i,1}\ge\cdots\ge a_{i,h}\ge0.
\tag{3.3}
\]

Put

\[
A_q=|\{i:a_{i,q}>0\}|.
\tag{3.4}
\]

### Theorem 3.1 (profile-capacity lower bound)

For every exact band SCD resolved into monotone queue atoms,

\[
\boxed{
\widehat{\mathfrak R}
:=2\sum_i d_{i,0}
=2\sum_{q=1}^hA_q
\ge
2\sum_{q=1}^h
\left\lceil\frac{N_q}{L}\right\rceil.
}
\tag{3.5}
\]

Its exact prefix word length is

\[
W+\widehat{\mathfrak R},
\tag{3.6}
\]

while writing one complete-residual sentinel per atom adds exactly
\(A_0\) entries. This is the complete-state convention, not a minimum over
arbitrary shared physical initializations.

### Proof

Theorem 2.1 gives exact prefix overhead \(2d_{i,0}\) for atom \(i\). Since

\[
d_{i,0}=\sum_{q=1}^h\mathbf1_{\{a_{i,q}>0\}},
\]

summing over atoms proves the identity in (3.5). At depth \(q\), exact SCD
ownership gives

\[
N_q=\sum_i a_{i,q}.
\tag{3.7}
\]

Each nonzero summand is at most \(\ell_i\le L\), so
\(N_q\le LA_q\), proving the lower bound. Finally
\(\sum_i\ell_i=W\), which gives (3.6), and writing one residual sentinel per
atom adds \(A_0\). \(\square\)

This is an exact invariant, not an expectation or an averaging statement.
It says that each depth row needs enough separately initialized atoms to
carry its \(N_q\) chains, even though all depths within one atom share the
same reset.

### Theorem 3.2 (sharp profile table and fractional multiframe cover)

Let \(L+h\le m\), put \(N_0=W\), and set

\[
J=\left\lceil\frac WL\right\rceil.
\]

For \(1\le j\le J\) and \(0\le q\le h\), define

\[
a_{j,q}
=\min\{L,(N_q-(j-1)L)_+\}.
\tag{3.8}
\]

There are integral nonincreasing profiles having these depth counts. They
attain equality in (3.5). Moreover, averaging the corresponding queue atoms
over all coordinate relabelings gives an exact fractional cover of every
mask in every band rank, with the same integral-profile reset mass.

If arbitrary nonnegative fractional weights on queue atoms are allowed,
the exact fractional optimum is instead

\[
\boxed{\frac2L\sum_{q=1}^hN_q.}
\tag{3.10a}
\]

### Proof

For each fixed \(j\), the sequence (3.8) is nonincreasing in \(q\). Put
\(\ell_j=a_{j,0}\) and define

\[
d_{j,t}=\max\{q:0\le q\le h,\ t<a_{j,q}\},
\qquad0\le t<\ell_j.
\tag{3.9}
\]

Then \(d_{j,t}\) is nonincreasing in \(t\), and precisely \(a_{j,q}\) of
its entries reach depth \(q\). Its maximum is at most \(h\), while
\(\ell_j\le L\), so Theorem 2.1 applies. Also

\[
\sum_{j=1}^Ja_{j,q}=N_q,
\qquad
|\{j:a_{j,q}>0\}|
=\left\lceil\frac{N_q}{L}\right\rceil.
\tag{3.10}
\]

This proves profile-level equality in (3.5).

For the fractional statement, average the labelled queue atom of profile
\(j\) uniformly over all permutations of the \(2m\) coordinates. At either
rank \(m-q\) or \(m+q\), it contains \(a_{j,q}\) distinct masks. Coordinate
transitivity therefore gives every fixed mask fractional load

\[
\frac{a_{j,q}}{N_q}
\]

from that normalized orbit. Summing over \(j\) and using (3.10) gives load
one. Thus every band mask is covered exactly fractionally, and the reset
mass is the equality value in (3.5).

For the unrestricted fractional optimum, let \(A_q^{\rm frac}\) be the
total fractional weight of atoms reaching depth \(q\). Each such atom
supplies at most \(L\) depth-\(q\) states, so exact fractional ownership
gives \(A_q^{\rm frac}\ge N_q/L\). The fractional reset cost is
\(2\sum_{q=1}^hA_q^{\rm frac}\), proving the lower bound in (3.10a).

For attainment, set \(N_{h+1}=0\). For each \(0\le r\le h\), take the
uniform coordinate orbit of a length-\(L\), constant-radius-\(r\) queue
atom with total weight

\[
w_r=\frac{N_r-N_{r+1}}L.
\tag{3.10b}
\]

At depth \(q\), the total atom weight is
\(\sum_{r=q}^hw_r=N_q/L\); the \(L\) masks supplied by every atom give each
rank-\((m-q)\) and rank-\((m+q)\) mask load one by coordinate transitivity.
Summation by parts gives reset cost

\[
2\sum_{r=0}^h r w_r
=\frac2L\sum_{q=1}^hN_q.
\]

This proves (3.10a). \(\square\)

The word “fractionally” is essential. Scaling the orbit averages gives an
exact integral multicover, but resolving it into mask-disjoint whole atoms
inside one SCD color is a separate hypergraph-resolution problem.

### Corollary 3.3 (Gaussian-window scale)

Fix \(A>0\), take

\[
h=\lceil A\sqrt m\rceil,
\qquad
L=m-h.
\tag{3.11}
\]

Then the minimum integral profile-table reset mass, equivalently the mass
of the corresponding orbit cover in Theorem 3.2, is

\[
\boxed{
2\sum_{q=1}^h\left\lceil\frac{N_q}{L}\right\rceil
=
\left(\sqrt\pi\,\operatorname{erf}(A)+o(1)\right)
\frac{W}{\sqrt m}.
}
\tag{3.12}
\]

In particular it is \(o(W)\).

The unrestricted fractional optimum (3.10a) has the same asymptotic,
because its difference from the displayed integral-profile value lies in
\([0,2h)\).

### Proof

Uniformly for \(q\le A\sqrt m+1\),

\[
\frac{N_q}{W}
=\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}
=\exp\left(-\frac{q^2}{m}+O_A(m^{-1})\right).
\tag{3.13}
\]

Therefore

\[
\begin{aligned}
2\sum_{q=1}^h\left\lceil\frac{N_q}{L}\right\rceil
&=\frac{2W}{L}\sum_{q=1}^h
  \left(e^{-q^2/m}+O_A(m^{-1})\right)+O(h)\\
&=\frac{2W\sqrt m}{m}
  \left(\int_0^Ae^{-x^2}\,dx+o(1)\right)\\
&=\left(\sqrt\pi\,\operatorname{erf}(A)+o(1)\right)
  \frac{W}{\sqrt m}.
\end{aligned}
\]

Here \(L/m\to1\), and the polynomial rounding error \(O(h)\) is negligible
relative to \(W/\sqrt m\). \(\square\)

Thus the corrected \(2d\) reset ledger reaches the required lower-order
scale before any integral SCD resolution is attempted. The missing
asymptotic theorem is not a better telescoping estimate.

## 4. An unconditional multiframe tour inside one exact product SCD

Let

\[
C=(L;z_1,\ldots,z_{2d};R),
\qquad1\le d<m,
\tag{4.1}
\]

be one chain in a full SCD of \(B_{2m}\), and add coordinates \(a,b\). The
standard phase-\(a\) SCD of the product box
\(C\times B_{\{a,b\}}\) consists of the four child chains

\[
\mathsf A
=(L;z_1,\ldots,z_{2d},a,b;R),
\tag{4.2}
\]

\[
\mathsf B
=(L+a;z_1,\ldots,z_{2d-1},b;R+z_{2d}),
\tag{4.3}
\]

\[
\mathsf D
=(L+b;z_1,\ldots,z_{2d};R+a),
\tag{4.4}
\]

and

\[
\mathsf C
=(L+a+b;z_1,\ldots,z_{2d-2};
  R+z_{2d-1}+z_{2d}).
\tag{4.5}
\]

Their radii are \(d+1,d,d,d-1\), respectively. For
\(1\le d<m\), these are the four components of the usual exact product SCD
of \(B_{2m+2}\). The zero-radius and terminal boundary boxes are treated
separately below; no fractional ownership or almost-matching is involved.

### Theorem 4.1 (exact four-chain multiframe braid)

There is one literal prefix word exposing the four child chains in the order

\[
\mathsf A,\ \mathsf D,\ \mathsf B,\ \mathsf C
\tag{4.6}
\]

with total length

\[
\boxed{4d+5.}
\tag{4.7}
\]

Hence its exact prefix overhead above the four designated chain endpoints is
\(4d+1\). Four independent exact hard starts have total length

\[
(2d+3)+(2d+1)+(2d+1)+(2d-1)=8d+4
\tag{4.8}
\]

and overhead \(8d\). The exact saving is

\[
\boxed{4d-1.}
\tag{4.9}
\]

### Proof

Initialize \(\mathsf A\) in \(2(d+1)+1=2d+3\) exact-prefix entries. Append

\[
L+b.
\tag{4.10}
\]

The new last-occurrence state begins

\[
L+b,z_1,\ldots,z_{2d},a,\ldots,
\tag{4.11}
\]

and hence exposes \(\mathsf D\). Now append, in the displayed order,

\[
z_{2d-1},z_{2d-2},\ldots,z_1,L+a.
\tag{4.12}
\]

After these \(2d\) updates, the state begins

\[
L+a,z_1,\ldots,z_{2d-1},b,z_{2d},\ldots,
\tag{4.13}
\]

so its first \(2d+1\) prefix unions expose \(\mathsf B\). Finally append

\[
L+a+b.
\tag{4.14}
\]

The resulting state begins

\[
L+a+b,z_1,\ldots,z_{2d-2},\ldots,
\]

and exposes \(\mathsf C\). The entry count is

\[
(2d+3)+1+2d+1=4d+5.
\]

Equations (4.8)--(4.9) follow by subtracting the four endpoint entries.
\(\square\)

For \(d=0\), the product box contains the radius-one chain \(\mathsf A\)
and the radius-zero singleton \(\mathsf D\). The update
\(\mathsf A\to\mathsf D\) gives length four, equal to two independent exact
starts; there is no saving.

Apply Theorem 4.1 in every box with \(1\le d<m\), use the preceding
two-chain length-four tour in every \(d=0\) box, and treat the single
terminal \(d=m\) box separately by the ordinary product decomposition and
the terminal word convention. These choices preserve one exact full child
SCD color, and the terminal contribution is \(O(m)\). This is therefore a
genuine exact-SCD special case, not an orbit average. However, summing
\(4d+1\) over the Gaussian distribution of positive nonterminal
parent-chain radii is still \(\Theta(W\sqrt m)\). The theorem halves the
leading local reset scale but does not make it \(o(W)\).

### Theorem 4.2 (recency-inversion lower bound)

Suppose a source last-occurrence state has a marker \(y\) more recent than
pairwise distinct singleton blocks

\[
x_1,\ldots,x_k,
\]

while a target chain exposure requires the singleton increments
\(x_1,\ldots,x_k\) all to be more recent than \(y\), with distinct final
occurrence times. Every literal bridge has at least \(k\) entries.

### Proof

If some \(x_i\) is never refreshed, it remains older than \(y\). Refreshing
\(y\) only makes the required inversion harder. Hence every \(x_i\) must
occur in the bridge. Distinct target singleton blocks cannot have equal last
occurrence times, so their final occurrences occupy distinct bridge entries.
\(\square\)

The \(\mathsf D\to\mathsf B\) switch in Theorem 4.1 has

\[
y=b,
\qquad
x_i=z_i\quad(1\le i\le2d-1).
\]

Thus Theorem 4.2 forces \(2d-1\) entries. In addition, \(a\) is older than
\(z_1\) in (4.11) but must belong to the new lower prefix \(L+a\), ahead of
\(z_1\). It needs one further occurrence, distinct from the singleton
refreshes. Therefore the bridge length is at least \(2d\), and (4.12) is
optimal.

This is the sharp local distinction: a monotone radius drop consumes stored
tail refinement and may cost one update, whereas this frame inversion moves
a marker across a depth-\(d\) recency queue and pays essentially the full
reset.

### Proposition 4.3 (compact-state radius variation)

Let \(b(\Pi)\) be the number of nonempty blocks in an ordered partition.
One MTF update satisfies

\[
b(M_X\Pi)\le b(\Pi)+1.
\tag{4.15}
\]

A compact nonterminal radius-\(d\) state has \(2d+2\) blocks. Hence every
nonempty exact-state bridge from a compact radius-\(d\) state to a compact
radius-\(e\) state has length at least

\[
\boxed{\max\{1,2(e-d)\}.}
\tag{4.16}
\]

Consequently a compact-state chronology with radii
\(d_1,\ldots,d_T\), bridge lengths \(b_i\), and a fresh exact-prefix start
has length

\[
T+2d_1+\sum_{i=1}^{T-1}(b_i-1)
\ge
T+2d_1+
\sum_{i=1}^{T-1}\bigl(2(d_{i+1}-d_i)-1\bigr)_+.
\tag{4.17}
\]

### Proof

Each update can split off at most its newly moved front block, proving
(4.15). Comparing \(2d+2\) source blocks with \(2e+2\) target blocks gives
the \(2(e-d)\) bound; a nonempty bridge costs at least one. Summing the
excess \(b_i-1\) beyond one endpoint entry proves (4.17). \(\square\)

The compactness hypothesis is indispensable. The queue atom deliberately
keeps stale singleton blocks in a refined tail. That stored block potential
is precisely what makes later prefix exposures cheaper than (4.16) would
predict from radius alone.

## 5. A depth-one invariant for every exact queue-resolved SCD

Let \(\mathcal A\) be an exact saturated band SCD resolved into monotone
queue atoms. In atom \(i\), let

\[
a_i=a_{i,1}
\]

be the number of its initial centers whose chains reach depth one, and put

\[
A_1=|\{i:a_i>0\}|.
\tag{5.1}
\]

Let \(\Lambda_m\) be the maximum number of edges in a linear forest
\(F\subseteq J(2m,m)\) such that the edge intersections are pairwise
distinct rank-\((m-1)\) sets and the edge unions are pairwise distinct
rank-\((m+1)\) sets. Call such an \(F\) two-sided rainbow.

### Theorem 5.1 (rainbow-linear reset invariant)

Every exact queue-resolved band SCD satisfies

\[
\boxed{
\widehat{\mathfrak R}
\ge2A_1
\ge2(N_1-\Lambda_m).
}
\tag{5.2}
\]

More precisely, its atoms canonically determine a two-sided-rainbow linear
forest with exactly

\[
N_1-A_1
\tag{5.3}
\]

edges.

### Proof

Write the centers of atom \(i\) as

\[
S_{i,0},S_{i,1},\ldots,S_{i,\ell_i-1}.
\]

For \(0\le t<a_i-1\), retain the Johnson edge

\[
e_{i,t}=S_{i,t}S_{i,t+1}.
\tag{5.4}
\]

The retained edges form vertex-disjoint paths because the atoms partition
the middle centers of the exact SCD. Their colors are

\[
S_{i,t}\cap S_{i,t+1}=C_{i,t}^{-1},
\tag{5.5}
\]

the lower depth-one member of chain \((i,t)\), and

\[
S_{i,t}\cup S_{i,t+1}=C_{i,t+1}^{+1},
\tag{5.6}
\]

the upper depth-one member of chain \((i,t+1)\). Exact SCD ownership makes
all masks in (5.5) distinct and all masks in (5.6) distinct. Thus the forest
is two-sided rainbow.

Its size is

\[
\sum_i(a_i-1)_+
=\sum_i a_i-A_1
=N_1-A_1,
\]

because exactly \(N_1\) band chains reach depth one. Hence
\(N_1-A_1\le\Lambda_m\). Every atom counted by \(A_1\) has
\(d_{i,0}\ge1\), so
\(\widehat{\mathfrak R}=2\sum_i d_{i,0}\ge2A_1\). This proves (5.2).
\(\square\)

Thus an \(o(W)\)-reset queue resolution would force

\[
\Lambda_m=N_1-o(W),
\tag{5.7}
\]

an almost-complete two-sided-rainbow linear forest. This requirement is
independent of the deeper-radius quota problem.

### Theorem 5.2 (robust reservoir obstruction)

Let \(E\) be any prescribed reservoir of Johnson edges, and let
\(\lambda(E)\) be the maximum size of a two-sided-rainbow linear subforest
of \(E\). If \(s\) of the canonical internal edges (5.4) lie outside
\(E\), then

\[
\boxed{
\widehat{\mathfrak R}+2s
\ge2(N_1-\lambda(E)).
}
\tag{5.8}
\]

### Proof

The internal forest has \(N_1-A_1\) edges. At most \(\lambda(E)\) of them
can lie in \(E\), so

\[
N_1-A_1-s\le\lambda(E).
\]

Use \(\widehat{\mathfrak R}\ge2A_1\) and rearrange. \(\square\)

### Corollary 5.3 (Greene--Kleitman multiframe no-go)

Let \(E_{\rm GK}\) be the directed projection-edge reservoir induced by
the Greene--Kleitman SCD.  Let \(\Delta_m\) be the exact rooted-plane-tree
deletion total from
`MATH_THEOREM_CATALAN_MATCHING_SWITCH_RECTANGLES_AND_GK_EDIT_DISTANCE_20260731.md`.
Then

\[
\lambda(E_{\rm GK})=m\operatorname{Cat}_m-\Delta_m
                  =N_1-\Delta_m,
\tag{5.9}
\]

and every exact queue resolution whose internal forest uses only \(s\)
edges outside this reservoir satisfies

\[
\boxed{
\widehat{\mathfrak R}+2s
\ge2\Delta_m.
}
\tag{5.10}
\]

In particular, \(s=o(W)\) forces
\[
 \widehat{\mathfrak R}
 \ge(2\mu-o(1))W,
 \qquad
 \mu=0.356895867892\ldots .
\]

### Proof

The full Greene--Kleitman reservoir is already two-sided rainbow, so every
edge subset remains two-sided rainbow.  Its components are exactly the
rooted plane trees with \(m\) edges.  The two-state rooted-tree DP in the
cited theorem retains exactly

\[
 m\operatorname{Cat}_m-\Delta_m
\]

edges under the degree-two constraint.  Because the reservoir is a forest,
degree at most two is equivalent to being a linear forest, proving (5.9).
The former \(W/2\) argument was false: deleting a vertex's outgoing edge can
leave two incoming edges, and incoming projection edges do not repeat the
global upper palette.

Finally,

\[
N_1=\binom{2m}{m-1}=W-\operatorname{Cat}_m.
\]

Substitution in (5.8) proves (5.10).  The cited generating-function theorem
gives \(\Delta_m/(m\operatorname{Cat}_m)\to\mu\), and
\(m\operatorname{Cat}_m=(1-o(1))W\), proving the asymptotic statement.
\(\square\)

Corollary 5.3 is stronger than a one-cut obstruction: it permits arbitrary
time dependence, arbitrarily many cuts, and arbitrary radius drops, but
charges every internal depth-one edge that leaves the prescribed branching
reservoir. It does not say that keeping Greene--Kleitman chain ownership
automatically keeps every internal edge in \(E_{\rm GK}\); that is an
additional, explicitly quantified hypothesis.

## 6. A complete exact queue-SCD instance

The integral resolution gate is already nonvacuous without appealing to a
search. The following explicit table gives a direct proof in the first
nontrivial band.

Let \(m=3\), let the coordinate set be \(\{0,1,2,3,4,5\}\), and take
\(h=1\), atom length two. A six-digit queue lists

\[
z_{-1},z_0,z_1,z_2,z_3,z_4.
\]

For a profile \(d_0d_1\), the table records the lower rank-two masks, the
two rank-three centers, and the upper rank-four masks exposed by that atom.
Concatenated digits denote sets.

| queue | profile | lower masks | centers | upper masks |
|---|---:|---|---|---|
| 301245 | 11 | 12, 24 | 012, 124 | 0123, 0124 |
| 134025 | 11 | 04, 02 | 034, 024 | 0134, 0234 |
| 250143 | 11 | 01, 14 | 015, 014 | 0125, 0145 |
| 250314 | 11 | 03, 13 | 035, 013 | 0235, 0135 |
| 124503 | 11 | 45, 05 | 245, 045 | 1245, 0245 |
| 135204 | 10 | 25 | 235, 025 | 1235 |
| 043512 | 11 | 35, 15 | 345, 135 | 0345, 1345 |
| 524310 | 10 | 34 | 234, 134 | 2345 |
| 413205 | 10 | 23 | 123, 023 | 1234 |
| 345120 | 00 | -- | 145, 125 | -- |

### Theorem 6.1 (exact \(B_6\) multiframe band SCD)

The twenty chains encoded by the table partition every mask in ranks two,
three, and four exactly once. They therefore form a saturated central-band
SCD and extend to a full SCD of \(B_6\). Their exact-prefix atom words have
total length

\[
\boxed{38.}
\tag{6.1}
\]

Starting all fifteen radius-one chains and five singleton chains separately
would have length

\[
20+2\cdot15=50.
\tag{6.2}
\]

Thus time-dependent two-chain braiding saves twelve literal entries while
retaining exact SCD ownership.

### Proof

The lower column is

\[
01,02,03,04,05,
12,13,14,15,
23,24,25,
34,35,45,
\]

the complete rank-two layer. The complements of the upper masks are,
respectively,

\[
45,35,25,15,34,23,14,24,03,13,04,12,02,01,05,
\]

again every pair exactly once. Sorting the center column gives

\[
\begin{gathered}
012,013,014,015,
023,024,025,
034,035,045,\\
123,124,125,134,135,145,
234,235,245,345,
\end{gathered}
\]

the complete rank-three layer. This proves exact band ownership directly.

Six profiles are \(11\), three are \(10\), and one is \(00\). Hence there
are fifteen radius-one chains and five singleton chains. By Theorem 2.1,
each of the first nine atoms has exact-prefix length
\(2+2=4\), while the last has length two. Their total is

\[
9\cdot4+2=38.
\]

Finally, every saturated symmetric-chain decomposition of a central band
extends to a full SCD. One proof extends one outer rank pair at a time: if
the current correlated boundary endpoints are \(A_y\subseteq B_y\), form
the bipartite graph between the new lower sets plus copies \(y^-\) and the
new upper sets plus copies \(y^+\). Join a new lower set to \(y^+\) when it
lies below \(A_y\), join \(y^-\) to a new upper set when it lies above
\(B_y\), and add the identity edge \(y^-y^+\). Giving comparison edges
weight \(1/(m+q+1)\) and identity edges weight
\((2q+1)/(m+q+1)\) makes every row and column sum one. Hall's theorem gives
an integral perfect matching, which extends or terminates every boundary
chain consistently. Iteration produces a full SCD. \(\square\)

The complete-state convention would add one residual sentinel per atom and
give length 48. Equation (6.1) is the corrected exact \(2d\) prefix ledger.
The extension may attach outer members to some band chains; the length-38
words expose the central-band restrictions, not all newly attached outer
masks. The full-SCD conclusion is an exact ownership statement, not a
length-38 full-cube cover.

## 7. Exact motion of the coordinate frame

For a radius-\(d\) state

\[
\omega=(L;z_1,\ldots,z_{2d};R),
\]

define its shell matching

\[
K(\omega)
=\bigl\{\{z_i,z_{2d+1-i}\}:1\le i\le d\bigr\}.
\tag{7.1}
\]

A perfect matching \(P\) of the \(2m\) coordinates is compatible with
\(\omega\) if \(K(\omega)\subseteq P\). This one frame simultaneously
pairs every nested central label, because

\[
\{z_{d-q+1},\ldots,z_{d+q}\}
\]

is the union of \(q\) edges of \(K(\omega)\) for every \(q\le d\).

For perfect matchings \(P,Q\), put

\[
\Delta(P,Q)=m-|P\cap Q|,
\tag{7.2}
\]

the number of matching edges replaced.

### Theorem 7.1 (sharp frame distance across one rotor step)

Let \(\omega\to\omega'\) be a nonterminal radius-\(d\) rotor edge,
\(1\le d<m\). For every compatible pair \(P\supseteq K(\omega)\),
\(Q\supseteq K(\omega')\),

\[
\boxed{\Delta(P,Q)\ge d+1.}
\tag{7.3}
\]

For every compatible \(P\), there is a compatible \(Q\) attaining equality.
The sharp choices can be made sequentially along an arbitrary rotor path.

### Proof

Write the successor as

\[
\omega'
=(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}).
\tag{7.4}
\]

The union \(K(\omega)\cup K(\omega')\) is one alternating path of
\(2d\) edges on the \(2d+1\) vertices

\[
x,z_1,\ldots,z_{2d},
\]

with endpoints \(x,z_{2d}\). None of its \(d\) old shell edges can belong
to \(Q\), and none of its \(d\) new shell edges can belong to \(P\). In the
symmetric difference of two perfect matchings, every alternating path must
be completed to an alternating cycle. Thus one further old edge incident
with \(x\) and one further new edge incident with \(z_{2d}\) must change.
This proves (7.3).

For sharpness, let \(r=P(x)\). Remove from \(P\) the \(d\) edges of
\(K(\omega)\) and the edge \(xr\); insert the \(d\) edges of
\(K(\omega')\) and the edge \(z_{2d}r\); leave every other edge fixed. The
result is a perfect matching \(Q\) compatible with \(\omega'\), and exactly
\(d+1\) edges changed. Since the construction starts with an arbitrary
compatible \(P\), it iterates. \(\square\)

The large value in (7.3) is not a reset charge. It is a combinatorial
distance between the coordinate frames that certify the nested shadows.

### Theorem 7.2 (sharp frame transport under a monotone radius step)

Consider one transition in Theorem 2.1 from radius \(d\) to radius
\(e\le d\). If \(e=0\), a compatible frame can be kept unchanged. If
\(e\ge1\), then every pair of compatible frames satisfies

\[
\boxed{\Delta(P,Q)\ge e+1,}
\tag{7.5}
\]

and equality is attainable sequentially.

### Proof

At time \(t\), the old singleton word is

\[
z_{t+d-1},z_{t+d-2},\ldots,z_{t-d},
\]

whereas at time \(t+1\) the new radius-\(e\) word is

\[
z_{t+e},z_{t+e-1},\ldots,z_{t+1-e}.
\]

Assume \(1\le e<d\), and put

\[
\mathcal C=\{z_{t-e-1},z_{t-e},\ldots,z_{t+e}\}.
\]

On \(\mathcal C\), the old reflection pairs indices summing to \(2t-1\)
and has \(e+1\) edges. The new reflection pairs indices summing to
\(2t+1\) and has \(e\) edges, leaving
\(z_{t-e-1},z_{t-e}\) free. The union is one alternating path. Every old
edge on \(\mathcal C\) meets the new shell, so none can be common to
compatible \(P,Q\); hence at least \(e+1\) edges change.

For equality, replace the old matching on \(\mathcal C\) by the new shell
plus the edge \(\{z_{t-e-1},z_{t-e}\}\), leaving \(P\) unchanged off
\(\mathcal C\). When \(e=d\), Theorem 7.1 gives the same value \(e+1\).
When \(e=0\), the new shell is empty and imposes no change. Each equality
construction begins with an arbitrary compatible \(P\), so it iterates
along the profile.
\(\square\)

### Corollary 7.3 (global frame-motion identity)

For an exact band SCD resolved into monotone atoms, choose the sharp
sequential frames of Theorem 7.2 at every internal transition. Then

\[
\boxed{
2\sum_{q=1}^hN_q-\widehat{\mathfrak R}
=2\sum_{\text{internal transitions }t}
  (\Delta_t-1)_+.
}
\tag{7.6}
\]

For arbitrary compatible frame choices, equality becomes \(\le\).

### Proof

In atom \(i\), the number of transitions whose next radius still reaches
depth \(q\) is \((a_{i,q}-1)_+\). Therefore, over all atoms,

\[
\#\{t:d_{t+1}\ge q\}
=N_q-A_q.
\tag{7.7}
\]

Summing the next radii by layers gives

\[
\sum_t d_{t+1}
=\sum_{q=1}^h(N_q-A_q).
\tag{7.8}
\]

Theorem 7.2 gives \((\Delta_t-1)_+=d_{t+1}\) for the sharp transport and at
least that much for arbitrary compatible transport. Finally use

\[
\widehat{\mathfrak R}=2\sum_{q=1}^hA_q.
\]

This proves (7.6). \(\square\)

For \(h=\lceil A\sqrt m\rceil\), if
\(\widehat{\mathfrak R}=o(W)\), then (3.13) and (7.6) force

\[
\boxed{
\sum_t(\Delta_t-1)_+
\ge
\left(\int_0^Ae^{-x^2}\,dx+o(1)\right)W\sqrt m.
}
\tag{7.9}
\]

Thus a low-reset resolution must move through coordinate frames at
Gaussian-scale total matching distance. The sharp construction proves that
this motion can occur without adding reset entries. Frame-switch count or
matching distance alone therefore cannot be charged as OR length; it is a
structural certificate of how nonstationary the missing integral resolution
must be.

There is nevertheless an exact obstruction when the time-dependent frames
must be drawn from one fixed finite library.

### Theorem 7.4 (fixed frame-library obstruction)

Let an exact band SCD be resolved into monotone queue atoms, and suppose
that every state is assigned a compatible perfect matching from a fixed
library of \(K\ge1\) matchings. Then

\[
\boxed{
\widehat{\mathfrak R}
\ge
2\sum_{\substack{1\le q\le h\\q>K/2}}
\left\lceil\frac{N_q}{K}\right\rceil .
}
\tag{7.10}
\]

Consequently, if \(h=\lceil A\sqrt m\rceil\) and
\(K/\sqrt m\to\kappa\in(0,2A)\), then

\[
\liminf_{m\to\infty}
\frac{\widehat{\mathfrak R}}{W}
\ge
\frac{2}{\kappa}
\int_{\kappa/2}^{A}e^{-x^2}\,dx>0.
\tag{7.11}
\]

If \(K=o(\sqrt m)\), then in fact

\[
\frac{\widehat{\mathfrak R}}{W}\longrightarrow\infty.
\tag{7.12}
\]

In particular, any such resolution with
\(\widehat{\mathfrak R}=o(W)\) must use

\[
K\ge(2A-o(1))\sqrt m.
\tag{7.13}
\]

### Proof

At time \(t\), if the state reaches depth \(q\), its inner \(q\)-shell is

\[
K_{t,q}
=
\bigl\{\{z_{t+j},z_{t-1-j}\}:0\le j<q\bigr\}.
\tag{7.14}
\]

Its support is the index interval
\([t-q,t+q-1]\), and its edges pair indices whose sum is \(2t-1\).
Suppose that times \(t\) and \(t+k\) both reach depth \(q\), where
\(0<k<2q\). The two support intervals overlap. If \(z_s\) is a coordinate
in their intersection, its mate in \(K_{t,q}\) is
\(z_{2t-1-s}\), whereas its mate in \(K_{t+k,q}\) is
\(z_{2(t+k)-1-s}\). These mates are distinct because \(k>0\) and all queue
coordinates are distinct. No perfect matching can therefore contain both
shells.

Now fix one atom \(i\). Its \(a_{i,q}\) states reaching depth \(q\) occur
at consecutive times. If \(a_{i,q}\ge K+1\), two of the first \(K+1\)
states receive the same library frame. Their positive time separation is at
most \(K<2q\), contradicting the preceding paragraph. Hence

\[
a_{i,q}\le K\qquad(q>K/2).
\tag{7.15}
\]

Exact ownership gives
\(N_q=\sum_i a_{i,q}\), so (7.15) implies
\(A_q\ge\lceil N_q/K\rceil\). Summing
\(\widehat{\mathfrak R}=2\sum_qA_q\) proves (7.10).

For \(K/\sqrt m\to\kappa\in(0,2A)\), the uniform central estimate

\[
\frac{N_q}{W}
=
\exp\!\left(-\frac{q^2}{m}+O_A(m^{-1})\right)
\tag{7.16}
\]

and a Riemann sum in (7.10) give (7.11). If \(K=o(\sqrt m)\), fix any
\(0<a<A\) and retain only \(a\sqrt m\le q\le A\sqrt m\). On this interval
\(N_q\ge(e^{-A^2}+o(1))W\), whence

\[
\frac{\widehat{\mathfrak R}}{W}
\ge
\left(2(A-a)e^{-A^2}+o(1)\right)
\frac{\sqrt m}{K}\longrightarrow\infty.
\]

Finally, if (7.13) failed along a subsequence, then a further subsequence
would have either \(K=o(\sqrt m)\) or
\(K/\sqrt m\to\kappa<2A\), contradicting (7.12) or (7.11) when
\(\widehat{\mathfrak R}=o(W)\). \(\square\)

In the fixed-window regime (indeed, whenever two such states fit in one
injective queue), the local threshold \(2q\) is sharp for this repetition
argument: at time separation \(2q\), the two \(q\)-shell supports are
disjoint, and their union extends to a perfect matching. Theorem 7.4 is
thus a library-size obstruction, not a universal reset lower bound when a
fresh frame may be chosen at every state.

## 8. Exact remaining lemma and implication scope

The natural integral target exposed by the preceding theorems is the
following.

> **Multiframe queue-SCD resolution \(\mathrm{MQSCD}_A\) -- UNPROVED.**  
> For every fixed \(A>0\), with
> \[
> h=\lceil A\sqrt m\rceil,
> \qquad L=m-h,
> \]
> there is one saturated SCD of the ranks \(m-h,\ldots,m+h\), partitioned
> into monotone queue atoms of length at most \(L\), such that
> \[
> \boxed{\widehat{\mathfrak R}=2\sum_i d_{i,0}=o(W).}
> \tag{8.1}
> \]

Theorem 2.1 would turn this into a literal band word of length \(W+o(W)\),
and the band-extension theorem would place the same band chains inside one
full integral SCD color. No separate factorability, pin, or fractional
ownership condition would remain inside the band.

Theorem 3.2 proves the exact fractional version of this statement with the
stronger toll \(O(W/\sqrt m)\). It does not prove (8.1), because its orbit
atoms overlap. The missing operation is an integral resolution of that
balanced multicover into mask-disjoint whole atoms while keeping their
chronologies intact.

A particularly sharp replacement lemma would realize the Ferrers profiles
(3.8) themselves. That would attain the capacity optimum (3.12). The weaker
statement (8.1) permits different profiles and is the smallest sufficient
lemma isolated here.

This fixed-window lemma is a multiframe SCD/MTF gate. By itself it is not
asserted to be equivalent to overload MWB, labelled common-owner
synchronization, or the original classwise rotor lemma. Its cross-radius
seams are legal MTF updates but not rotor arcs. Completing a full
coefficient-one OR proof would additionally require the already-audited
diagonal window and tail bookkeeping, or a growing-window version with an
appropriate shared tail word.

## 9. Final theorem ledger

### Proved

1. Exact nonincreasing-radius queue atoms have literal length
   \(\ell+2d_0\), and their hard-reset toll telescopes exactly as in (2.14).
2. Exact queue-SCD resolutions obey the Ferrers capacity invariant (3.5).
3. The capacity bound is attained by integral profile data and by a
   corresponding exact fractional coordinate-orbit cover. The unrestricted
   fractional optimum is (3.10a); both have reset scale
   \(\Theta_A(W/\sqrt m)\).
4. Every positive nonterminal parent box in the standard product SCD has
   the exact multiframe tour (4.6), saving \(4d-1\) entries relative to
   independent starts. Radius zero has its separate length-four,
   zero-saving tour; the single terminal box contributes only \(O(m)\)
   under its separate terminal convention.
5. Recency inversion forces the \(2d\) product-frame bridge, and compact
   states obey the radius-variation bound (4.17).
6. Every exact queue-SCD resolution induces a depth-one two-sided-rainbow
   linear forest and satisfies (5.2).
7. Relative to the Greene--Kleitman edge reservoir, the robust bound is
   \(\widehat{\mathfrak R}+2s\ge W-2\operatorname{Cat}_m\).
8. The displayed ten atoms form an exact central-band SCD of \(B_6\), extend
   to one full SCD, and realize exact-prefix length 38 rather than 50.
9. Compatible coordinate frames move by at least \(e+1\) matching edges at
   every positive-radius monotone step, sharply and sequentially; the global
   conservation law is (7.6).
10. Arbitrary time-dependent alternation among a fixed library of \(K\)
    frames obeys (7.10); an \(o(W)\)-reset fixed-\(A\sqrt m\) resolution
    needs at least \((2A-o(1))\sqrt m\) distinct frames.

### Not proved

- \(\mathrm{MQSCD}_A\), or any asymptotic integral queue-atom resolution.
- A nontrivial universal numerical upper bound
  \(\Lambda_m\le N_1-cW\); without it, (5.2) is a structural invariant, not
  a universal \(\Omega(W)\) reset theorem.
- An \(o(W)\) recursion from the product-box braid; its total remains
  \(\Theta(W\sqrt m)\).
- \(\mathrm{RSCD}_A\), overload MWB, or the contiguous-OR conjecture.

## 10. Adversarial audit

1. **Exact versus conservative toll.** Every principal word length uses the
   exact prefix convention and omits the residual block. Writing a complete
   residual sentinel adds one entry per hard-started atom. No \(2d+1\)
   charge is hidden inside \(\widehat{\mathfrak R}\).
2. **Refined tails.** After a radius drop the full ordered partition is
   generally not compact. Only its required chain prefix is controlled.
   This is sufficient for literal suffix ORs but not for an argument that
   demands one compact residual block.
3. **Architecture scope.** The identities
   \(\widehat{\mathfrak R}=2\sum A_q\) and (5.2) concern decompositions into
   genuinely nonincreasing queue atoms with one hard reset each. They are not
   identities for arbitrary SCD chronologies.
4. **No conflict with rotor no-averaging.** Same-radius pieces of an atom are
   rotor runs; its radius-drop seams are not. The radiuswise rotor theorem
   therefore does not prohibit (2.14).
5. **Fractional gap.** Theorem 3.2 gives a fractional cover or, after common
   scaling, an integral multicover. Neither is one exact SCD color. The
   distinction is the principal unresolved gate.
6. **Product scope.** The boxwise construction using Theorem 4.1 together
   with the separate radius-zero and terminal treatments is one exact
   full-SCD construction, but its saving is only a constant-factor
   reduction of a \(\Theta(W\sqrt m)\) ledger.
7. **Recency scope.** Theorem 4.2 is exact for the stated inversion pattern;
   it is not a lower bound for every possible change of coordinate frame.
8. **Compact-state potential.** Proposition 4.3 cannot be applied to a
   refined source by replacing its true block count with \(2d+2\). Retained
   tail granularity is a real resource.
9. **Rainbow invariant.** The unconditional quantity \(\Lambda_m\) may in
   principle equal \(N_1\). The numerical Greene--Kleitman bound assumes
   that all but \(s\) internal edges stay in that explicitly prescribed
   reservoir; keeping Greene--Kleitman chain ownership alone does not imply
   this.
10. **Frame motion is not word length.** The Gaussian lower bound (7.9)
    measures matching-edge replacements between compatible analytical
    frames. The sharp transport realizes those changes without extra MTF
    entries, so (7.9) is not an OR lower bound.
11. **Frame-library scope.** Theorem 7.4 permits arbitrary alternation but
    assumes one globally fixed library. A construction that chooses a fresh
    frame at each state evades its hypothesis. The \(2q\) threshold is a
    repeated-frame obstruction, not a matching-distance charge.
12. **Small exact case.** The \(B_6\) table proves one finite exact SCD
    instance directly. It supplies no asymptotic rounding theorem.
13. **Terminal radius.** All local formulas assume \(d<m\). No terminal
    \(2m-1\) convention is extrapolated into these window arguments.

After these qualifications, the stable conclusion is that the corrected
\(2d\) toll can telescope to the right asymptotic scale, but only through a
highly nonstationary integral SCD resolution. The exact remaining obstacle
is mask-disjoint multiframe atomization, not reset arithmetic.
