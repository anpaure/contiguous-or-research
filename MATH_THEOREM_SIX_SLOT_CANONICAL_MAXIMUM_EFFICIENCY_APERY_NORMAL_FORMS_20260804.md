# Six-slot Bellman clocks: canonical maximum-efficiency Apéry normal forms

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It gives the exact
first-crossing, endpoint-saturation, least-maximizer partition at the first
open grid size, derives an availability-filtered Apéry normal form in every
branch, sharpens the `h=2,3,4,5` branches, and invokes the independently
audited complete closures of the `h=2` and `h=6` branches.  It does not
prove complete six-slot positivity or the all-grid Bellman inequality.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 (c_0,c_1,\ldots,c_6),\qquad c_0=0,
\tag{0.1}
\]

be nonnegative and internally superadditive.  Its Bellman clock is

\[
 V_0=0,\qquad
 V_m=\max_{1\le j\le\min(m,6)}(c_j+V_{m-j}),
\tag{0.2}
\]

and its functional is

\[
                         \Phi(c)=\sum_{m\ge0}K(V_m).
\tag{0.3}
\]

For a period `P` and shifts, write

\[
 \mathcal L_h(P;s_1,\ldots,s_{h-1})
 =\sum_{q\ge0}\left(K(qP)+\sum_{r=1}^{h-1}K(qP+s_r)\right).
\tag{0.4}
\]

## 1. Canonical six-slot counterexample normalization

### Proposition 1.1

If a nonpositive six-slot Bellman table exists, then one exists satisfying

\[
 c_1,c_2,c_3,c_4,c_5<A\le c_6,
\tag{1.1}
\]

and

\[
 c_6=\max\{A,P_6\},
 \qquad
 P_6=\max\{c_1+c_5,c_2+c_4,2c_3\}.
\tag{1.2}
\]

Assign such a table to

\[
 h=\min\operatorname*{argmax}_{2\le j\le6}{c_j\over j}.
\tag{1.3}
\]

Then

\[
                         h\in\{2,3,4,5,6\}.
\tag{1.4}
\]

If `h=6`, necessarily

\[
                         c_6=A.
\tag{1.5}
\]

#### Proof

Apply first-crossing deletion.  If the first threshold crossing had index
at most five, the authenticated complete five-slot theorem would make the
resulting prefix strictly positive, contradicting proof-safe deletion.
Thus the first crossing is at six, giving (1.1).

Endpoint saturation gives `c_6=max(A,P_6)`.  Every lower partition of six
can be collapsed by superadditivity to two complementary parts, so

\[
 P_6=\max_{1\le i\le5}(c_i+c_{6-i}),
\]

which is exactly (1.2).

Internal superadditivity gives `c_2>=2c_1`.  Therefore if size one has
maximum density then size two does as well, and the restricted least
maximizer (1.3) loses no table.  Finally, if (1.3) selects size six, no
lower positive size has its density; the least-critical endpoint theorem
therefore gives (1.5). \(\square\)

The order in this proposition is essential:

\[
 \text{first crossing}\longrightarrow
 \text{endpoint saturation}\longrightarrow
 \text{least maximizer}.
\tag{1.6}
\]

Endpoint saturation can change the maximizing density branch.

## 2. Exact availability-filtered Apéry form

Fix a branch `h` from (1.4), and put

\[
 \lambda={c_h\over h},\qquad P=c_h,
 \qquad d_j=c_j-j\lambda\le0.
\tag{2.1}
\]

On `Z/hZ`, allow a directed step labelled `j` for every
`j in {1,...,6}\setminus{h}`.  Its residue is `j mod h`, its ordinary
capacity is `j`, and its reduced weight is `d_j`.  For a simple path `Q`
from zero to residue `r`, write

\[
 \ell(Q)=\sum_{j\in Q}j,
 \qquad d(Q)=\sum_{j\in Q}d_j.
\tag{2.2}
\]

Define

\[
 \beta_r(m)=\max\{d(Q):Q\text{ simple from }0\text{ to }r,
                              \ \ell(Q)\le m\}.
\tag{2.3}
\]

### Theorem 2.1

For every `m>=0`, with `r=m mod h`,

\[
                         \boxed{V_m=\lambda m+\beta_r(m).}
\tag{2.4}
\]

Let

\[
 M_h=\max(\{1,2,3,4,5,6\}\setminus\{h\}),
 \qquad L_h=(h-1)M_h.
\tag{2.5}
\]

Then

\[
 (L_2,L_3,L_4,L_5,L_6)=(6,12,18,24,25).
\tag{2.6}
\]

All simple paths are available once `m>=L_h`.  If

\[
 \beta_r=\max_Qd(Q),\qquad s_r=r\lambda+\beta_r,
 \qquad \widehat V_{qh+r}=qP+s_r,
\tag{2.7}
\]

then

\[
\boxed{
 \Phi(c)=\mathcal L_h(P;s_1,\ldots,s_{h-1})
 +\sum_{m=0}^{L_h-1}\bigl(K(V_m)-K(\widehat V_m)\bigr).
}
\tag{2.8}
\]

#### Proof

Read an exact-fill configuration as a residue walk.  Its value is
`lambda*m` plus its reduced weight.  Whenever a residue repeats, delete
the intervening closed segment.  That segment has capacity divisible by
`h` and nonpositive reduced weight, so deletion does not decrease the
reduced weight.  The resulting simple path proves the upper bound in
(2.4).

Conversely, pad any path admitted in (2.3) by `(m-ell(Q))/h` copies of
the size-`h` generator.  This proves equality.  A simple path uses at most
`h-1` edges, each of capacity at most `M_h`, proving (2.5)--(2.6).
Splitting the exact functional from its stabilized formal lattice gives
(2.8). \(\square\)

Thus every six-slot branch is a finite head plus at most six exact
Gaussian cosets; there is no unstructured infinite recursion.

## 3. The size-two branch: one new scalar wedge

Write

\[
 (c_1,c_2,c_3,c_4,c_5,c_6)=(x,y,z,w,T,U)
\]

and suppose `h=2`.  Maximal efficiency and superadditivity force

\[
                         w=2y,\qquad U=3y.
\tag{3.1}
\]

Put

\[
                         s=T-2y.
\tag{3.2}
\]

Then

\[
 {A\over3}\le y<{A\over2},
 \qquad
 0\le x\le z-y\le s\le {y\over2},
 \qquad s<A-2y.
\tag{3.3}
\]

The exact clock is

\[
 V_{2q}=qy,qquad V_1=x,qquad V_3=z,qquad
 V_{2q+1}=qy+s\quad(q\ge2),
\tag{3.4}
\]

and hence

\[
\boxed{
 \Phi=\mathcal L_2(y;s)+K(x)-K(s)+K(z)-K(y+s).
}
\tag{3.5}
\]

Both finite corrections are nonnegative.  Indeed,

\[
 0\le x\le s<{A\over4},
 \qquad z\le y+s\le {3y\over2}<{3A\over4},
\]

and `K` is decreasing through `3A/4`.  Therefore the complete `h=2`
branch is reduced to the single scalar gate

\[
\boxed{
 \mathcal L_2(y;s)>0
 \quad\left(
 {A\over3}\le y<{A\over2},\quad
 0\le s\le\min\{y/2,A-2y\}
 \right).
}
\tag{3.6}

The endpoint `s=A-2y` is adjoined harmlessly to the sufficient compact
gate.  The already-proved five-slot wedge covers the part
`2A/5<=y<A/2`, `A-2y<=s<=y/2`; (3.6) is its complementary small-shift
face and is genuinely new at grid six.

The independently audited three-compact-row theorem proves (3.6) on its
entire domain.  It retains the `q=0,1,2` compact derivative rows, bounds
the remaining tail by one Gaussian integral, and uses concavity to reduce
the scalar region to three positive boundary rows.  Therefore

\[
                         \boxed{\Phi>0\quad\text{throughout }h=2.}
\tag{3.7}
\]

#### Proof of the normal form

The equalities (3.1) follow from
`c_4>=2c_2`, `c_6>=3c_2` and the reverse maximum-density bounds.
First crossing then gives `2y<A<=3y`.  Also

\[
 z\ge x+y,qquad T\ge y+z,qquad T\le{5y\over2},
\]

which gives (3.3), including `s<A-2y` from `T<A`.

Among odd residue representatives, size three dominates size one and
size five dominates size three in reduced weight.  The latter becomes
available at capacity five.  Even capacities use only the critical size
two, proving (3.4), and subtraction of the two unavailable formal entries
gives (3.5).

## 4. The size-three branch: the exact five-pulse gate returns

Put

\[
 p=c_3,qquad a=c_4-p,qquad b=c_5-p.
\tag{4.1}
\]

In the `h=3` branch,

\[
 c_6=2p,qquad {A\over2}\le p<A,
\tag{4.2}
\]

and

\[
 c_1\le a\le {p\over3},qquad
 c_2\le b\le {2p\over3},qquad
 a,b<A-p.
\tag{4.3}
\]

The two eventual shifts are

\[
 s_1=\max\{a,2b-p\},
 \qquad s_2=\max\{b,2a\}.
\tag{4.4}
\]

Define

\[
 V_7=\max\{p+c_4,c_5+c_2\},
 \qquad V_8=\max\{2c_4,p+c_5\}.
\tag{4.5}
\]

Then the exact functional is

\[
\boxed{
\begin{aligned}
 \Phi={}&\mathcal L_3(p;s_1,s_2)\\
 &+K(c_1)-K(s_1)
  +K(c_4)-K(p+s_1)
  +K(V_7)-K(2p+s_1)\\
 &+K(c_2)-K(s_2)
  +K(c_5)-K(p+s_2).
\end{aligned}}
\tag{4.6}
\]

The proof is the three-residue simple-path calculation.  Size four
dominates size one in residue one, size five dominates size two in residue
two, and size six is the zero-reduced critical loop `2p`.  The double
size-five and double size-four witnesses first appear at capacities ten
and eight, respectively, giving exactly the five displayed availability
pulses.  This is algebraically the five-slot `h=3` normal form, but its
domain is new: here both `c_4,c_5` are below `A` and the first crossing is
the inert critical value `c_6=2p`.

## 5. The size-four branch: twelve eventual linear forms

Put

\[
 P=c_4,qquad e=c_5-P,
\tag{5.1}
\]

and define the best eventual nonzero-residue weights

\[
 d_1=e-{P\over4},qquad
 d_2=c_6-{3P\over2},qquad
 d_3=c_3-{3P\over4}.
\tag{5.2}
\]

Here

\[
 {2A\over3}\le P<A.
\tag{5.3}
\]

Size five dominates size one in residue one because
`c_5>=P+c_1`; size six dominates size two in residue two because
`c_6>=P+c_2`.  Therefore the stabilized Apéry weights are

\[
\boxed{
\begin{aligned}
 \beta_1&=\max\{d_1,d_2+d_3,d_1+2d_2,3d_3\},\\
 \beta_2&=\max\{d_2,2d_1,2d_3,d_1+d_2+d_3\},\\
 \beta_3&=\max\{d_3,d_1+d_2,3d_1,2d_2+d_3\}.
\end{aligned}}
\tag{5.4}
\]

With `s_r=rP/4+beta_r`, the exact branch is

\[
\boxed{
 \Phi=\mathcal L_4(P;s_1,s_2,s_3)
 +\sum_{m=0}^{17}\bigl(K(V_m)-K(\widehat V_m)\bigr).
}
\tag{5.5}
\]

Every head value is the literal maximum (2.4); in particular, the early
size-one and size-two representatives are retained before their better
congruent size-five and size-six representatives become available.

## 6. The size-five branch: sixty-four eventual linear forms

Put

\[
 P=c_5,qquad e=c_6-P,
 \qquad d_1=e-{P\over5},
 \qquad d_j=c_j-{jP\over5}\quad(2\le j\le4).
\tag{6.1}
\]

Then

\[
 {5A\over6}\le P<A,
 \qquad 0\le e\le {P\over5}.
\tag{6.2}
\]

Size six dominates size one in residue one because `c_6>=P+c_1`.
The effective residue graph therefore has one best step of each nonzero
residue `1,2,3,4`, with reduced weights `d_1,d_2,d_3,d_4`.

For each nonzero target residue, a simple path is specified by an ordered
list of distinct intermediate vertices chosen from the other three
nonzero residues.  Hence it has

\[
                         1+3+3\cdot2+3\cdot2\cdot1=16
\tag{6.3}
\]

path words.  Across the four target residues this gives sixty-four
displayed linear forms.  Let `beta_r` be their maxima and put
`s_r=rP/5+beta_r`.  Then

\[
\boxed{
 \Phi=\mathcal L_5(P;s_1,s_2,s_3,s_4)
 +\sum_{m=0}^{23}\bigl(K(V_m)-K(\widehat V_m)\bigr).
}
\tag{6.4}
\]

Again the head in (6.4) is exact and retains every early representative.
Unlike the five-slot endpoint branch, the period `P=c_5` is below `A`;
the crossing is carried by `c_6`.  This subthreshold five-coset carry is
the first geometry not removable by the complete five-slot theorem.

One canonical headless subface is already closed.  The affine setup-cost
table

\[
 {A\over10}(0,1,3,5,7,9,10)
\tag{6.5}
\]

lies simultaneously on all three inert endpoint faces and has exact
period `9A/10`.  Its selected residues modulo nine are
`{0,1,3,5,7}`.  The independently audited omitted-residue theorem proves
that the complementary even-residue train is smaller than `-1/100`, and
hence

\[
                         \boxed{\Phi_{\rm affine}>{1\over100}.}
\tag{6.6}
\]

Thus the exact no-descent example is not itself a Bellman separator.  The
rest of the `h=5` branch remains open.

## 7. The size-six branch is completely positive

If `h=6`, Proposition 1.1 gives `c_6=A`.  The endpoint-period comparison
is literal:

\[
 \Phi(c)\ge C(A)+\sum_{i=1}^{5}F_A(c_i).
\tag{7.1}
\]

Endpoint superadditivity gives

\[
 c_1+c_5\le A,qquad c_2+c_4\le A,qquad2c_3\le A.
\tag{7.2}
\]

The independently audited subcomplementary-pair theorem applies to the
first two pairs, while `F_A(c_3)>0`.  It proves the strict bound

\[
                         \boxed{\Phi(c)>{163\over70000}>0.}
\tag{7.3}
\]

Thus no normalized nonpositive six-slot table lies in the endpoint-
efficient branch.

## 8. Exact frontier and scope

After proof-safe normalization, a possible six-slot counterexample is
assigned to exactly one of `h=3,4,5`; both `h=2` and `h=6` are closed.
Its exact infinite clock is one of (4.6), (5.5), or (6.4), each with every
availability transient retained.

The structurally newest face is the subthreshold five-coset carry (6.4).
No claim of positivity is made for the three surviving branches, for
every six-slot table, for arbitrary grid size, or for an OR-word upper
bound.

## 9. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| all-grid first crossing, saturation, Apéry reduction | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| least-critical endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete positivity through five slots | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| independent five-slot aggregate audit | `MATH_AUDIT_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_INDEPENDENT_20260804.md` | `8e853c0b47b177129a25a4a28741d42ca2f5df665775cd6cc074a604e2de8d9f` |
| six-slot two-efficient closure | `MATH_THEOREM_SIX_SLOT_TWO_EFFICIENT_COMPLETE_THREE_COMPACT_ROW_CLOSURE_20260804.md` | `53a65d72f9f6a22ccef91f43c5759c61fc0a0ea831294b71b56a46d1cae95d3a` |
| independent two-efficient audit | `MATH_AUDIT_SIX_SLOT_TWO_EFFICIENT_COMPLETE_THREE_COMPACT_ROW_CLOSURE_INDEPENDENT_20260804.md` | `900b1a3201ae3738736b470887e483700be1d89966ec4ded12a70f30632c6ac4` |
| six-efficient closure | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| independent six-efficient audit | `MATH_AUDIT_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_INDEPENDENT_20260804.md` | `1045aba0ab3a372f0e822f9e61702e600240c73eee61faa1916676a4790c7f8b` |
| affine no-descent family | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| independent affine no-descent audit | `MATH_AUDIT_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_INDEPENDENT_20260804.md` | `bb6de7fc9468fbdc988df0ca7e3cc07ac5f1787ec4d0cd17f8afb0a4357b5443` |
| affine Beatty omitted-residue closure | `MATH_THEOREM_SIX_SLOT_AFFINE_BEATTY_OMITTED_RESIDUE_CLOSURE_20260804.md` | `0bfc91a873e559234f89231abeb6f14ef30ef43c7b727e8a8c391e7e0e0b5c46` |
| independent Beatty closure audit | `MATH_AUDIT_SIX_SLOT_AFFINE_BEATTY_OMITTED_RESIDUE_CLOSURE_INDEPENDENT_20260804.md` | `214f0000148cedc7fe3b6772c71f0a930482ad70460240a4163dc004dd7958a4` |
