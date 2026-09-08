# Independent audit: canonical six-slot maximum-efficiency Apéry normal forms

**Date:** 2026-08-04  
**Verdict:** **GO.**  The normalization order, endpoint partition value,
availability-filtered Apéry theorem, branch domains, eventual residue
forms, finite-head cutoffs, and frozen positive subfaces are correct.  The
current revision additionally invokes the independently audited complete
`h=2` closure; no core normal-form formula changed.  No theorem byte was
changed during this audit.

## 1. Exact binding

Audited theorem:

`MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md`

SHA-256:

`3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede`

Every dependency hash in its frozen table matches the current workspace:

| role | SHA-256 |
|---|---|
| all-grid first crossing/saturation/Apéry theorem | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| least-critical endpoint normalization | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete positivity through five | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| independent five-slot audit | `8e853c0b47b177129a25a4a28741d42ca2f5df665775cd6cc074a604e2de8d9f` |
| complete six-slot size-two branch | `53a65d72f9f6a22ccef91f43c5759c61fc0a0ea831294b71b56a46d1cae95d3a` |
| independent size-two audit | `900b1a3201ae3738736b470887e483700be1d89966ec4ded12a70f30632c6ac4` |
| complete six-efficient branch | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| independent six-efficient audit | `1045aba0ab3a372f0e822f9e61702e600240c73eee61faa1916676a4790c7f8b` |
| affine no-descent family | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
| independent affine audit | `bb6de7fc9468fbdc988df0ca7e3cc07ac5f1787ec4d0cd17f8afb0a4357b5443` |
| affine Beatty closure | `0bfc91a873e559234f89231abeb6f14ef30ef43c7b727e8a8c391e7e0e0b5c46` |
| independent Beatty audit | `214f0000148cedc7fe3b6772c71f0a930482ad70460240a4163dc004dd7958a4` |

## 2. Canonical normalization

First-crossing deletion is used in the proof-safe direction.  A crossing
before slot six would yield a nonpositive prefix of grid at most five,
contradicting the frozen complete theorem.  Hence a possible counterexample
has

\[
 c_1,\ldots,c_5<A\le c_6.
\]

For every lower partition of six, choose one part `i` and merge all
remaining parts by superadditivity.  Its value is at most
`c_i+c_{6-i}`, and every complementary pair is feasible.  Thus

\[
 P_6=\max\{c_1+c_5,c_2+c_4,2c_3\}
\]

exactly.  Endpoint saturation precedes least-maximizer assignment, as it
must.

The restricted least maximizer among sizes `2,...,6` is exhaustive because
`c_2>=2c_1`.  If it selects size six, none of sizes `2,...,5` ties its
density; size one cannot tie either, again by `c_2>=2c_1`.  Hence size six
is the global least maximizer and the least-critical endpoint theorem
legitimately gives `c_6=A`.

## 3. Availability-filtered Apéry theorem

An exact fill of capacity `m` is a residue walk of reduced value
`value-lambda*m`.  Every repeated-residue segment has capacity divisible
by `h` and nonpositive reduced weight.  Removing it cannot lower the
reduced value, so a maximizing witness may be simple.  Conversely, when
`m` has the target residue, `m-ell(Q)` is a nonnegative multiple of `h`;
padding by size-`h` critical generators proves equality.

The size-one path reaches every residue and has capacity at most `m`, so
the filtered maximum is never empty at a relevant `m`.  A simple path has
at most `h-1` edges, each of capacity at most

\[
 M_h=\max(\{1,\ldots,6\}\setminus\{h\}).
\]

Therefore the exact safe cutoffs are

\[
 (L_2,L_3,L_4,L_5,L_6)
 =(1\cdot6,2\cdot6,3\cdot6,4\cdot6,5\cdot5)
 =(6,12,18,24,25).
\]

The finite-head ranges `0<=m<L_h` and all displayed sums ending at
`L_h-1` are consequently correct.

## 4. Size-two branch

Maximal size-two density and internal superadditivity force

\[
 c_4=2c_2=2y,qquad c_6=3c_2=3y.
\]

First crossing gives `A/3<=y<A/2`.  With `s=c_5-2y`,

\[
 0\le c_1=x\le c_3-y=z-y\le s\le y/2,
 \qquad s<A-2y.
\]

In the odd residue, size three dominates size one and size five dominates
size three.  The size-five representative first appears at capacity five;
all even capacities use critical size-two value.  Hence

\[
 V_{2q}=qy,quad V_1=x,quad V_3=z,quad
 V_{2q+1}=qy+s\ (q\ge2),
\]

and exactly the two corrections in the theorem remain.

The corrections have the correct nonnegative sign: `x<=s<A/4` and
`z<=y+s<3A/4`, while `K` decreases on the whole interval through
`3A/4`.  The compact scalar domain

\[
 A/3\le y<A/2,qquad
 0\le s\le\min\{y/2,A-2y\}
\]

is the closure of the honest strict domain; adjoining
`s=A-2y` is harmless for a sufficient inequality.

The current theorem now invokes the independently audited
three-compact-row theorem on exactly this domain.  That result proves the
scalar lattice strictly positive while retaining both finite corrections;
hence the added conclusion `Phi>0` on the complete `h=2` branch is valid.

## 5. Size-three branch

Maximal density gives `c_6<=2c_3`, and superadditivity gives the reverse,
so `c_6=2p`.  First crossing yields `A/2<=p<A`.  The definitions
`a=c_4-p`, `b=c_5-p` and the density/prefix conditions give exactly

\[
 c_1\le a\le p/3,qquad
 c_2\le b\le2p/3,qquad a,b<A-p.
\]

Modulo three, size six is a zero-residue critical loop and introduces no
new simple path.  Size four dominates size one; size five dominates size
two.  The double size-five residue-one witness first fits at capacity ten,
and the double size-four residue-two witness first fits at capacity eight.
The values `V_7,V_8`, eventual shifts, and five availability pulses are
therefore exactly the displayed five-slot normal form on the new domain.

## 6. Size-four branch

The range `2A/3<=P<A` follows from
`A<=c_6<=6P/4`.  Size five dominates size one in residue one, and size six
dominates size two in residue two.  Their reduced weights are exactly

\[
 d_1=c_5-5P/4,qquad d_2=c_6-6P/4,qquad
 d_3=c_3-3P/4.
\]

The four simple-path weight forms for each target residue are precisely

\[
\begin{aligned}
 \beta_1&=\max\{d_1,d_2+d_3,d_1+2d_2,3d_3\},\\
 \beta_2&=\max\{d_2,2d_1,2d_3,d_1+d_2+d_3\},\\
 \beta_3&=\max\{d_3,d_1+d_2,3d_1,2d_2+d_3\}.
\end{aligned}
\]

The general cutoff is `L_4=18`, so the literal head `m=0,...,17` is
correct and retains the early size-one and size-two representatives.

## 7. Size-five branch

From `A<=c_6<=6P/5` and `P=c_5<A`,

\[
 5A/6\le P<A,qquad0\le e=c_6-P\le P/5.
\]

Superadditivity `c_6>=c_5+c_1` makes size six the eventual best
residue-one step.  The other best nonzero-residue steps are sizes two,
three, and four, with exactly the four displayed reduced weights.

For a fixed nonzero target in `Z/5Z`, a simple path is specified by an
ordered subset of the other three nonzero vertices.  The count is

\[
 1+3+3\cdot2+3\cdot2\cdot1=16.
\]

Thus there are sixty-four linear forms across four targets.  The cutoff is
`L_5=24`, so the exact head ends at capacity 23.  The theorem correctly
retains early size one before size six becomes available.

The affine table and omitted-residue closure are bound to their current
independently audited bytes.  Their conclusion is only the strict positive
subface `Phi_affine>1/100`; the theorem correctly leaves the rest of the
size-five branch open.

## 8. Size-six branch and scope

For the genuine size-six branch, least-critical normalization gives
`c_6=A`.  The independently audited endpoint-period/pair theorem gives
the literal strict margin `163/70000`; the normal-form theorem does not
rederive or enlarge that result.

Thus the surviving normalized branches are exactly `h=3,4,5`; both `h=2`
and `h=6` are closed.  Every eventual clock and finite availability head
displayed for the surviving branches is exact.  The theorem makes no
complete six-slot, all-grid, or OR-word claim.
