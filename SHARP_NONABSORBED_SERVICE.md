# Sharp service bound for every nonabsorbed short-hull seam

## 1. Local theorem

Fix consecutive directed internal peak plateaux `P=[u_0,v]` and
`P'=[u,v']` in an ordering of `H_a`.  Let their normalized edge costs and
strict intervening gap be

\[
 p={\lambda(P)\over a},\qquad
 s={\lambda(P')\over a},\qquad
 z={g\over a}.
\]

Assume `p,s in [1,2]`, the seam is nonabsorbed in the inherited
seam-local-maximum sense, and its hull is short:

\[
                         p+s+z\le4+o(1).              \tag{1.1}
\]

Then the starts in the predecessor edge-interior and strict gap have a
span-`(4a+3)` assignment of leading normalized cost

\[
 C_N(p,s,z)=p\min(s,z)+z\min(p,s).                   \tag{1.2}
\]

Moreover,

\[
 \boxed{C_N(p,s,z)\le{4\over3}(p+z),}                \tag{1.3}
\]

with equality only at

\[
                         p=s=z={4\over3}.             \tag{1.4}
\]

Thus every nonabsorbed short-hull record is subcritical at the exact average
cost `4a/3`; the unique neutral local geometry is the balanced triple.

## 2. Seam-local run

Let `d` be the strictly rising cross-coordinate on `P`, and put

\[
 M=\max_{v\le j\le u} d(T_j).
\]

Take a maximal component `R` of the superlevel set `{d>=M}` meeting a
maximizer in `[v,u]`.  The strict rise on `P` prevents `R` from extending
left of `v`.

If `d(T_u)<M`, the component closes before `u`.  If equality holds, then on
the directed plateau `P'` the coordinate `d` is falling, fixed, or rising.

* Falling closes the component at `u`.
* Fixed at level `M` is exactly absorption.
* Rising would finish above `a`, because strict integer rise on the two
  plateaux gives `d(T_(v'))>=lambda(P)+lambda(P')-a>a` in the dangerous
  regime.

Nonabsorption therefore supplies a full-word internal threshold run

\[
                  R\subseteq[v,u],\qquad
                  \lambda(R)\le g+1.                 \tag{2.1}
\]

This is the audited seam-local maximum lemma; intermediate maxima, partial
later plateaux, and shared endpoints do not change it.

Assign the `lambda(P)` predecessor edge-interior starts to the cheaper of
`R` and `P'`.  Assign every strict-gap start to the cheaper of `P` and `P'`.
The short-hull condition places all chosen runs within one-sided span
`4a+3`.  Shared endpoints and integer `+1` terms contribute only `O(a^2)`
after summing `O(a)` long seams.  Equation (1.2) follows.

## 3. Sharp algebra

It remains to prove (1.3), or equivalently

\[
                         3C_N\le4(p+z).              \tag{3.1}
\]

There are four order cases.

### Case 1: `p<=s` and `z<=s`

Here `C_N=2pz`.  Put `r=min(p,z)` and `t=max(p,z)`.  Feasibility gives
`r+2t<=4`, hence `r<=4/3`.  Maximizing in `t` reduces (3.1) to

\[
 3r^2-10r+8=(3r-4)(r-2)\ge0.                       \tag{3.2}
\]

### Case 2: `p<=s` and `z>=s`

Now `C_N=p(s+z)`.  Since `z>=(s+z)/2` and `p+s+z<=4`, it is enough to check

\[
                  (4-p)(3p-2)\le4p,
\]

again equivalent to `(3p-4)(p-2)>=0`.  Here `3p<=4`, so it holds.

### Case 3: `s<=p` and `z<=s`

Now `C_N=z(p+s)`.  The preceding argument with `p` and `z` exchanged gives

\[
                  (4-z)(3z-2)\le4z,
\]

and `3z<=4`.

### Case 4: `s<=p` and `z>=s`

Here `C_N=s(p+z)`, while

\[
                         3s\le p+s+z\le4.
\]

So (3.1) is immediate.  Equality in every slack step forces (1.4).

## 4. Global absorbed/bad-hull dichotomy

At one fixed threshold, split short-hull seams into nonabsorbed and absorbed
measures `rho_N,rho_A`.  Let `b` be normalized word mass in bad records and
the boundary, and use the mass identity

\[
 \int(p+z)d(\rho_N+\rho_A)+b=3.                     \tag{4.1}
\]

For absorbed seams use the neighbouring peaks, of cost

\[
 C_A(p,s,z)=ps+z\min(p,s).                          \tag{4.2}
\]

Define

\[
 \Delta_N={4\over3}(p+z)-C_N\ge0,
 \qquad
 \Delta_A=C_A-{4\over3}(p+z).                      \tag{4.3}
\]

Combining the local assignments with universal fallback on bad mass gives

\[
 {Q\over a^3}
 \le4-\int\Delta_Nd\rho_N+int\Delta_Ad\rho_A
       +{2\over3}b+o(1).                            \tag{4.4}
\]

Absorption requires `p+s<=3`.  Elementary optimization on
`1<=p,s<=2`, `z>=0`, and `p+s+z<=4` gives

\[
                         \Delta_A\le{2\over3},       \tag{4.5}
\]

with its maximum at `(p,s,z)=(1,2,0)`.  Therefore a word with
`D=o(a^2)`, for which every admissible assignment has
`Q>=(4-o(1))a^3`, must satisfy

\[
 \boxed{
\int\Delta_Nd\rho_N
 \le {2\over3}\bigl(\|\rho_A\|+b\bigr)+o(1).}       \tag{4.6}
\]

For completeness, if `min(p,s)<=4/3`, the coefficient of `z` in
`Delta_A` is nonpositive, so take `z=0`; maximizing
`p(s-4/3)` under `p+s<=3` gives `2/3` at `(1,2)`.  If both lengths exceed
`4/3`, take `z=4-p-s`.  In the regions `p<=s` and `s<=p`, direct
substitution bounds the result respectively by `4/9` and `5/12`.  This
proves (4.5) and its equality statement.

All strict saving on nonabsorbed short seams must be paid for by absorbed
seam mass or bad/boundary mass.  If both are negligible, the seam law forces
concentration at the neutral triple (1.4).  The inherited atomic seal excludes
the mass-two atom there, but it does not exclude every possible atomic mass;
Section 6 records the surviving mass-`9/8` equality ledger.

## 5. Bad-mass estimate at the bottom threshold

Put `delta=3-ell`.  A bad internal seam satisfies

\[
                         z>(2-p)+(2-s)+o(1).         \tag{5.1}
\]

Line uniqueness bounds the number of plateaux with `2-p<=r`, while the
total complement-gap budget is `delta a^2+o(a^2)`.  Splitting bad seams
according to whether one endpoint lies within `r` of length two or the gap
exceeds the remaining threshold, then optimizing `r`, gives

\[
 {N_{bad}\over a}\le2\sqrt{6\delta}+o(1),
 \qquad
 b\le4\sqrt{6\delta}+\delta+o(1).                   \tag{5.2}
\]

This estimate is useful together with the small-deficit wedge seal, but it
does not alone control the absorbed mass in (4.6).

## 6. Remaining target

The broad problem has been reduced to a three-way alternative:

1. absorbed short-hull seams, which must pay in positive-line geometry;
2. bad long-hull mass, bounded by (5.2) but not yet eliminated for general
   `delta`; or
3. concentration near `(4/3,4/3,4/3)`.

A universal proof now needs one joint inequality coupling these three
payments, plus an equality-case theorem for the neutral triple.  Purely
scalar gap or length moments are insufficient.

There is an exact coherent **scalar** equality ledger showing why the old
functional alone could not close the last clause:

\[
 \rho={9\over8}\,\delta_{(4/3,4/3,4/3)},
 \qquad \alpha=0,\qquad b=0.                        \tag{6.1}
\]

It has

\[
 \int(p+z)d\rho=3,\qquad
 \ell={3\over2},\qquad
 \int C_Nd\rho=4.                                  \tag{6.2}
\]

For every `1<c<4/3`, its first-dangerous functional is

\[
 U(c)=5-{3c\over4}\ge4.                             \tag{6.3}
\]

It also passes the unlabelled full-line/coarea relaxation, for example with
equal direction measures on `[-3/16,3/16]`.  However, the dangerous-list
self-closure theorem in `DANGEROUS_LIST_SELF_CLOSURE.md` now rules out every
physical realization: the hidden seam run has cost at most `ca` at each
fixed `c<4/3`, giving strict total cost below four.  The ledger remains a
sharp counterexample only to the older scalar-gap service functional.
