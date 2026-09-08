# Final audit of the monotone-profile rotor-packing gate

## Verdict

The local rotor theorem is valid (with the refined-state correction in
`MONOTONE_RADIUS_ROTOR_BRAIDS_AUDIT.md`).  It gives genuine OR words, so no
factorability or pin condition remains inside an atom.  The fractional
profile cover is also valid.

The proposed integral lemma is sufficient only after restoring its omitted
rank-incidence quotas.  It is not supplied by a standard matching or design
theorem.  More importantly, it is stronger than the OR problem requires: it
asks for an almost-disjoint SCD of the whole band, whereas rank-defect
accounting only asks that the total number of missing masks be `o(W)`.

For OR coverage, the claimed cross-depth sharing was already present in one
fixed radius-`h` long-run atom: each radius-`h` chain exposes every depth
`0,...,h`, the `H` centers use the same `H` MTF updates, and the reset is
already only `2h+1`.  The genuinely new content of the monotone-radius
theorem is selective truncation of those chains so that their incidences can
match SCD quotas.  That is useful for the stronger near-SCD packing, but it
does not improve the weak missing-only OR accounting by itself.

The exact pair parameters explain the gap.  A queue row has normalized
same-rank codegree `Theta(m^-2)`, but adjacent nested rows have normalized
codegree `(2+o(1))/m`.  A typical all-band atom has
`(sqrt(pi)+o(1)) m^(3/2)` vertices.  Hence the full atom has both

```text
edge_size * normalized_pair_codegree = Theta(sqrt(m))
```

and a full-codegree parameter tending to one.  None of the fixed-uniformity
nibbles audited in `GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT.md` applies in this
diagonal regime, and independent sampling is Poisson-collision dominated.

The `m=3` certificate is valid and is stronger than a coverage certificate:
it is an exact central-band SCD grouped into ten monotone queue atoms.  It is
useful evidence and a regression test, but it supplies no asymptotic
rounding theorem.

## 1. Exact labelled-orbit degrees

Put `n=2m`, take `H=m-h`, and fix one integral profile

\[
 H=a_0\ge a_1\ge\cdots\ge a_h\ge0.
\]

Use a labelled queue permutation.  At either sign and depth `q`, the atom
contains `a_q` intervals of length

\[
 k=m-q\quad\hbox{or}\quad k=m+q.
\]

For a fixed `k`-set `S`, the number of labelled queues containing `S` in
that row is exactly

\[
 \boxed{D_q(S)=a_q k!(n-k)!.}                       \tag{1.1}
\]

Indeed, the `a_q` possible interval positions are disjoint events, and for
each position the elements inside and outside the interval can be ordered in
`k!(n-k)!` ways.

If two distinct `k`-sets have Johnson distance `r`, their exact codegree is

\[
 \boxed{
 D_q(S,T)=
 2(a_q-r)_+(r!)^2(k-r)!(n-k-r)! .}                 \tag{1.2}
\]

Consequently

\[
 \boxed{
 {D_q(S,T)\over D_q(S)}=
 {2(a_q-r)_+\over
  a_q\binom kr\binom{n-k}r}.}                      \tag{1.3}
\]

Uniformly for `q<=h=o(m)`, the largest same-row ratio is therefore

\[
 (2+o(1))m^{-2}.                                   \tag{1.4}
\]

These counts are unchanged after passing from labelled queues to distinct
orbit atoms: degrees and codegrees are divided by the same stabilizer.
Notice also that one fixed profile orbit is regular only within each rank;
its absolute degrees vary between ranks.  The fractional theorem equalizes
the rows by mixing profile orbits with prescribed weights.  A black-box
unweighted matching theorem would first need a uniform, lossless conversion
of that weighted mixture, which is already part of the missing rounding
problem.

## 2. Exact nested cross-depth codegrees

Let `0<=q<r<=h`, put `b=r-q`, `A=a_q`, and `B=a_r`.
For two fixed lower-row masks

\[
 T\subset S,qquad |S|=m-q,\quad |T|=m-r,
\]

the number of compatible pairs of atom positions is

\[
 P^-_{q,r}=\sum_{j=0}^{b}\min\{B,(A-j)_+\}.         \tag{2.1}
\]

Thus

\[
 \boxed{
 {D(S,T)\over D(S)}=
 {P^-_{q,r}\over A\binom{m-q}{b}}.}                \tag{2.2}
\]

For the two upper rows, with `S subset T`, the corresponding position count
is

\[
 P^+_{q,r}=\sum_{j=0}^{b}(B-j)_+,                  \tag{2.3}
\]

and

\[
 \boxed{
 {D(S,T)\over D(S)}=
 {P^+_{q,r}\over A\binom{m-q}{b}}.}                \tag{2.4}
\]

For adjacent depths these specialize to

\[
 P^-_{q,q+1}=B+\min(B,A-1),\qquad
 P^+_{q,q+1}=2B-1.                                 \tag{2.5}
\]

Under the fractional profile law,
`E a_q=H binom(2m,m-q)/W`, so throughout the useful shallow band

\[
 {D(S,T)\over D(S)}=(2+o(1))m^{-1}                 \tag{2.6}
\]

for an adjacent intended chain pair.  Formula (2.1) follows by writing the
smaller interval start as `s=t-j`, `0<=j<=b`; (2.3) follows similarly from
`s=t+j`.  For each legal position pair, the factorial count cancels to the
binomial denominator displayed above.

The lower-to-upper formula is analogous.  If their depths are `q,r`, put
`b=q+r`; the compatible position count is

\[
 P^{-,+}_{q,r}=\sum_{j=0}^{b}\min\{a_q,(a_r-j)_+\}, \tag{2.7}
\]

and divide by
`a_q binom(m+q,b)`.  Hence no cross-sign pair is larger than the adjacent
ratios in (2.6).

## 3. Why the available black boxes stop here

For the profile distribution used in the proposal,

\[
 \begin{aligned}
 \mathbb E K
 &=H\left(1+2\sum_{q=1}^{h}
       {\binom{2m}{m-q}\over\binom{2m}m}\right)\\
 &=(\sqrt\pi+o(1))H\sqrt m
  =(\sqrt\pi+o(1))m^{3/2}                         \tag{3.1}
 \end{aligned}
\]

when `h/sqrt(m)->infinity` and `H=(1-o(1))m`.  Combining (2.6) and (3.1)
gives

\[
 K\,\Delta_2/\Delta_1=\Omega(\sqrt m).             \tag{3.2}
\]

There is also a decisive high-order obstruction to treating a complete atom
as an unstructured edge.  The labelled orbit degree is at most `(2m)!`
times the polynomial-size profile support, so `log D=O(m log m)`.  A whole
atom has codegree at least one.  Therefore any full-codegree parameter `B`
whose definition includes

\[
 B\le (D/\Delta_K)^{1/(K-1)}
\]

satisfies

\[
 B\le\exp(O(\log m/\sqrt m))=1+o(1).               \tag{3.3}
\]

Thus the full-codegree nibble has no growing reservoir here.  The audited
Pippenger--Rodl, Grable, Vu, Kang--Kuehn--Methuku--Osthus, and
Gould--Kelly statements either fix the uniformity or lose their useful rate
when `K` grows.  Even a theorem leaving merely `o(V)` vertices uncovered is
insufficient: the band has

\[
 V=(\sqrt\pi+o(1))W\sqrt m,
\]

whereas literal repair permits only `o(W)` misses, i.e. a relative leftover
`o(m^-1/2)`.

Independent atom sampling is much worse.  With `W/H` independent atoms,
each fixed band mask has asymptotic `Poisson(1)` multiplicity.  Hence

\[
 \mathbb E\sum D_q
   =(\sqrt\pi/e+o(1))W\sqrt m,                     \tag{3.4}
\]

and the middle row alone has `(e^-1+o(1))W` duplicate excess with
exponentially high probability.  Random sampling plus collision deletion is
therefore not a rounding proof.

## 4. Correct form of the strong integral lemma

For every sign and depth let `T_q^sigma` be total incidence, `D_q^sigma`
duplicate excess, and `M_q^sigma` the number missing.  Then exactly

\[
 \boxed{M_q^\sigma=N_q+D_q^\sigma-T_q^\sigma.}      \tag{4.1}
\]

At `q=0` the two signs denote the same middle row and are counted only once.

The strong monotone-profile lemma must require all three conditions

\[
 \begin{gathered}
 A=W/H+o(W/H),\\
 T_q^\sigma=N_q+O(W/H)\quad\hbox{for every }q,\sigma,\\
 D_0+\sum_{q=1}^{h}(D_q^-+D_q^+)=o(W).             \tag{4.2}
 \end{gathered}
\]

Atom count and duplicate mass alone do not imply the quotas: an
undersupplied row can have zero duplicates and still miss almost every
mask.  Scalar quota rounding is cheap (the common-uniform profile
distribution has support at most `h+1`), but the near-disjoint correlated
packing in the last line of (4.2) is unproved.

With `omega=log m`,

\[
 h=\lceil\sqrt{m\log m}\rceil,\qquad H=m-h,
\]

the proved truncated-tail theorem applies, `Ah=o(W)`, and (4.1)--(4.2)
would indeed imply `nu(2m)=W+o(W)`.  The broader submitted range
`omega=o(m)` is not justified by the currently proved tail theorem; its
uniform range is `omega=o(m^(1/3))`.

## 5. A strictly weaker sufficient queue lemma

The OR accounting never requires `D_q=o(W)`.  For any queue-atom family it
is enough that

\[
 A H=W+o(W),\qquad A h=o(W),\qquad
 \boxed{\sum_{q,\sigma}M_q^\sigma=o(W).}            \tag{5.1}
\]

No per-rank SCD quota and no near-disjointness is needed.  In overlap form,
(5.1) is

\[
 \sum_{q,\sigma}
   \bigl(D_q^\sigma-(T_q^\sigma-N_q)\bigr)=o(W).   \tag{5.2}
\]

For example, use the constant full-radius profile `d_t=h`.  Then
choose `A` so that `AH=W+O(H)`.  Thus `T_q^sigma=AH` at every
depth, and the total scalar rounding error `O(hH)` is polynomial and hence
`o(W)`.  The sufficient condition becomes

\[
 \sum_{q,\sigma}
   \bigl(D_q^\sigma-(W-N_q)\bigr)=o(W).             \tag{5.3}
\]

The large term `W-N_q` is unavoidable redundancy, not a defect.  Thus
(5.1) can hold while the strong duplicate sum in (4.2) is as large as
`Theta(Wh)` for the full-radius family.  The proposed monotone-profile packing lemma is
therefore strictly stronger than necessary at the scalar level.

This constant profile is exactly the fixed-radius long-run atom already
available before the monotone-profile theorem.  Thus the weak lemma (5.1),
not the quota-exact lemma (4.2), is the direct continuation of the older OR
route.

Equation (5.3) is the linear-queue analogue of the incremental-overlap
identity for the weak vertical wreath lemma in
`GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT.md`.  The published
Muetze--Standke--Wiechert theorem already supplies an exact odd-dimensional
middle wreath factor, so that route starts with the middle row solved and
asks only for

\[
 \sum_q M_q=o(W).
\]

It does **not** prove this vertical property: a published factor already
misses first-shadow targets at `m=4`.  Hence MSW does not close the weaker
queue lemma.  But the previously isolated weak vertical wreath lemma remains
the less demanding known sufficient target in coverage accounting; the new
near-SCD rotor gate does not replace it as the unique or weakest remaining
theorem.

## 6. The exact `m=3` certificate

For

\[
 m=3,\qquad h=1,\qquad H=2,
\]

`scratch/verify_rotor_packing_m3.py` contains ten queue atoms.  Their profile
multiset is

```text
6 copies of (1,1), 3 copies of (1,0), 1 copy of (0,0).
```

Hence the middle incidence is `10*2=20=binom(6,3)` and the depth-one
incidence is

```text
6*2 + 3*1 = 15 = binom(6,2) = binom(6,4).
```

Direct enumeration verifies every rank-2, rank-3, and rank-4 mask exactly
once.  Reconstructing the actual MTF initialization and update word gives
ten genuine factor words of total length 48 (nine of length five and one of
length three), whose suffix ORs include all 50 central-band masks.  Thus the
certificate is an exact central-band SCD grouped into monotone queue paths,
not merely a formal set cover.

The literal factor reconstruction is independently checked by
`scratch/verify_rotor_packing_m3_factor.py`.

The verifier hash at audit time was

```text
a065ff2b05064df6e607cb157963166eb259dbf80a89f4544c87d863f6f41012
472deb93389bc73d179150b7814d7951d097b313d6d39f108be1504056aa4777
```

The first hash is the set-packing verifier and the second is the literal MTF
factor verifier.

This proves that the integral gate is nonvacuous in its first instance.  It
does not provide the lossless multiscale correlation needed as `m` grows.

## 7. Sharp current boundary

The strongest justified conclusion is:

* variable-radius queues remove the local MTF/reset/pin obstruction;
* the exact fractional band cover exists;
* an exact small integral packing exists for `m=3`;
* generic random or black-box matching arguments do not deliver the required
  `o(W)` total defect; and
* the strong integral lemma is an approximate queue-compatible SCD theorem,
  while the weaker missing-only lemma (5.1) is sufficient for OR arrays.

Proving either the weak queue lemma (5.1) or the existing weak vertical
wreath lemma would finish the constant-one upper bound after the audited
tail and parity transfers.  No such integral theorem is currently proved.
