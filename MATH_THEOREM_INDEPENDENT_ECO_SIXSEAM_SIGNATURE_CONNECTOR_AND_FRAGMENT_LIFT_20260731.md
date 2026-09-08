# The all-six ECO block has union-transparent literal connectors, but no contracted two-sided connector

Date: 2026-07-31  
Lane: independent audit of full prefix/suffix signatures on the repaired ECO six-seam geometry  
Status: exact positive contracted connector theorem; exact two-sided contracted obstruction; exact retained-fragment profile reduction.  No claim that an arbitrary supplied ECO forest has the required fragment profiles.

## 0. Verdict

The full prefix/suffix OR lemma is correct.  Applied to the actual twelve
physical owners of one all-six coherent ECO atom, it gives a positive local
packet rather than a no-go:

* among the `25` literal Johnson perfect matchings on the twelve owners which
  avoid the old and new ECO edges, exactly `6` close **both** phases to a
  twelve-cycle;
* every one of those `6` has a choice of cut and orientation for which the
  two twelve-letter words have identical ordered prefix and suffix unions;
* `3` of the `6` can additionally be cut so that the old and new **internal**
  interval-union supports agree and the old and new internal
  interval-intersection supports agree.

Thus the local all-six geometry itself is compatible with the new
union-boundary signature.  There is an explicit length-twelve
OR-boundary-equivalent packet whose internal union and intersection banks are
coverage-equal.

The stronger simultaneous signature

\[
 \Sigma_\pm(X)=\bigl(\Sigma_\vee(X),
                       \Sigma_\vee(\overline X)\bigr)             \tag{0.1}
\]

does **not** survive.  In fact no common contracted endpoint pairing at all,
Johnson or otherwise, can make both phases Hamilton and have equal
`Sigma_+-`.  This is a short structural obstruction, not an experimental
failure.  It says that one cannot make every crossing union and every
crossing intersection pointwise invariant in the literal alternating
twelve-owner packet.

This does not refute a buffered ECO packet.  When the six common retained
endpoint pairs are expanded into nontrivial paths, their interiors can alter
the first and last occurrence times.  Section 5 gives the exact finite lift
criterion.  The actual buffered-path question is therefore instance
dependent and remains open until those six path profiles are exported.

## 1. The signature lemma and its two-sided version

For a word `X=(X_1,...,X_h)`, put

\[
 P_j^\vee(X)=\bigcup_{i\le j}X_i,
 \qquad
 S_j^\vee(X)=\bigcup_{i\ge j}X_i.                    \tag{1.1}
\]

The ordered pair of the two sequences is `Sigma_vee(X)`.  If equal-length
fragments `X,Y` have equal `Sigma_vee`, then replacing `X` by `Y` preserves
the value and address of every interval crossing either fragment boundary.
The proof in
`MATH_THEOREM_FULL_PREFIX_SUFFIX_SIGNATURE_UPPER_TRANSPARENCY_20260731.md`
is complete: a crossing interval is an unchanged exterior word OR one
prefix, one suffix, or the total union of the fragment.

Applying the same statement to complements proves the simultaneous form.
Equality of `Sigma_+-(X)` is equivalent to pointwise equality of all four
ordered chains

\[
 P_j^\vee,quad S_j^\vee,quad
 P_j^\cap=\bigcap_{i\le j}X_i,quad
 S_j^\cap=\bigcap_{i\ge j}X_i.                       \tag{1.2}
\]

It therefore preserves every crossing union and intersection.  This
two-sided condition is strictly stronger than union transparency.

## 2. The exact contracted ECO geometry

Use the notation of the repaired ECO six-seam theorem.  Remove the common
core `H-{e}` and abbreviate the twelve rank-`m` owners as

\[
\begin{array}{lll}
 X_a=H+a+d,&X_b=H+b+d,&X_c=H+c+d,\\
 Y_{ab}=H+a+b,&Y_{bc}=H+b+c,&Y_{ca}=H+c+a,\\
 U_{ab}=\infty+(H-e)+a+b,&U_{bc}=\infty+(H-e)+b+c,
   &U_{ca}=\infty+(H-e)+c+a,\\
 V_a=\infty+H+a,&V_b=\infty+H+b,&V_c=\infty+H+c.
\end{array}                                                    \tag{2.1}
\]

The two six-edge matchings are

\[
\begin{aligned}
 E_0={}&\{X_aY_{ca},X_bY_{ab},X_cY_{bc},
          U_{ab}V_b,U_{bc}V_c,U_{ca}V_a\},\\
 E_1={}&\{X_aY_{ab},X_bY_{bc},X_cY_{ca},
          U_{ab}V_a,U_{bc}V_b,U_{ca}V_c\}.
                                                               \tag{2.2}
\end{aligned}
\]

They are disjoint perfect matchings on the same twelve vertices.  Every
displayed edge is a Johnson edge.

Call a perfect matching `M` on these twelve vertices a **contracted common
connector** when `M` is disjoint from `E_0 union E_1`.  It is
simultaneously Hamiltonian when both `E_0 union M` and `E_1 union M` are
single twelve-cycles.  A linearization is obtained by choosing a direction
and deleting one cycle edge.

The complete finite counts are

| class | count |
|---|---:|
| all perfect matchings on twelve vertices | 10,395 |
| disjoint from `E_0 union E_1` | 3,328 |
| simultaneously Hamiltonian | 1,368 |
| admitting equal `Sigma_vee` linearizations | 194 |
| admitting equal `Sigma_+-` linearizations | **0** |
| disjoint literal-Johnson connector matchings | 25 |
| literal-Johnson and simultaneously Hamiltonian | 6 |
| literal-Johnson and equal `Sigma_vee` | **6** |
| literal-Johnson and equal `Sigma_+-` | **0** |

The audit in Section 7 exhausts the `11!!` matchings directly.  The positive
existence statement below does not depend on trusting the count.

## 3. One explicit union-transparent packet

Take the common Johnson matching

\[
\begin{split}
 M_*={}&\{X_aX_b, X_cV_c, Y_{ab}U_{ab},
          Y_{bc}V_b, Y_{ca}V_a, U_{bc}U_{ca}\}.
                                                               \tag{3.1}
\end{split}
\]

Every edge in (3.1) exchanges exactly one coordinate.  Both unions with
(2.2) are twelve-cycles.  Cut the common edge `Y_ab U_ab` and orient the two
resulting Hamilton paths as

\[
\begin{split}
 W_0={}&(
 U_{ab},V_b,Y_{bc},X_c,V_c,U_{bc},U_{ca},V_a,
 Y_{ca},X_a,X_b,Y_{ab}),\\
 W_1={}&(
 U_{ab},V_a,Y_{ca},X_c,V_c,U_{ca},U_{bc},V_b,
 Y_{bc},X_b,X_a,Y_{ab}).                            \tag{3.2}
\end{split}
\]

Every consecutive pair in `W_i` is an edge of `E_i union M_*`.  After
removing the common core, their common prefix-union chain is

\[
 ab\infty, eab\infty, eabc\infty,
 eabcd\infty,ldots,eabcd\infty,                    \tag{3.3}
\]

and their common suffix-union chain is

\[
 eabcd\infty,ldots,eabcd\infty, eabcd, eabd,eabd,eab.
                                                               \tag{3.4}
\]

Thus

\[
                         \Sigma_\vee(W_0)=\Sigma_\vee(W_1).    \tag{3.5}
\]

The packet has the same first owner `U_ab` and last owner `Y_ab` in both
phases, so it is also topologically compatible with a common exterior
attachment at those two boundary owners.

There are `78` internal intervals in either word.  In both phases their OR
support has `25` masks and their intersection support has `25` masks, and

\[
 \{\operatorname{OR}(I):I\subseteq W_0\text{ interval}\}
 =
 \{\operatorname{OR}(I):I\subseteq W_1\text{ interval}\},      \tag{3.6}
\]

\[
 \{\operatorname{AND}(I):I\subseteq W_0\text{ interval}\}
 =
 \{\operatorname{AND}(I):I\subseteq W_1\text{ interval}\}.    \tag{3.7}
\]

These are unary coverage equalities, not addresswise or multiplicity
equalities.  The OR multiplicities have five units of loss and five of gain;
the intersection multiplicities have two units of loss and two of gain.
Hence (3.6)--(3.7) must be recorded separately from the common support and
from crossing transparency.  Three of the six literal Johnson connectors
have a cut with both equalities; the other three retain exact internal
intersection support but exchange one internal OR target.

## 4. No contracted connector has the two-sided signature

The zero in the fourth row of the table has a short proof.

### Lemma 4.1 (two initial chains determine the second letter)

If two words have equal prefix unions and prefix intersections at lengths
one and two, then their first two letters agree pointwise.  The analogous
suffix statement determines their last two letters.

#### Proof

The length-one union gives the common first letter `A`.  If `U=A union B`
and `I=A intersection B`, then

\[
                             B=I\cup(U\setminus A).              \tag{4.1}
\]

Thus the common length-two union and intersection recover `B`.  Reverse the
words for the suffix statement.  \(\square\)

### Theorem 4.2 (contracted two-sided no-go)

Let `M` be any common connector matching disjoint from `E_0 union E_1` such
that both `E_0 union M` and `E_1 union M` are Hamilton cycles.  No two
linearizations of those cycles have equal `Sigma_+-`.

#### Proof

Suppose two such linearizations existed.  Lemma 4.1 says their first
directed edge is the same and their last directed edge is the same.  Since
the two cycles have common edge set exactly `M`, both displayed edges lie in
`M`.

The omitted closing edge joins the common last owner to the common first
owner.  At the first owner, the used first edge is its unique `M` edge, so
the other incident cycle edge--the omitted edge--lies in `E_i`.  The same
holds at the last owner.  Therefore the same omitted edge belongs to both
`E_0` and `E_1`, contradicting `E_0 intersection E_1=emptyset`.
\(\square\)

For the explicit packet (3.2), the failure is already visible at the
second prefix intersection:

\[
 U_{ab}\cap V_b=(H-e)+\infty+b,qquad
 U_{ab}\cap V_a=(H-e)+\infty+a.                    \tag{4.2}
\]

Equation (3.7) shows why this does not create an internal coverage loss:
the two values reappear at other internal addresses.  It only prevents
pointwise crossing-intersection transport.

## 5. Exact lift to nontrivial retained fragments

Endpoint contraction is not sound for arbitrary full signatures.  The
right lift state is nevertheless finite and elementary.

For a word fragment `F=(F_1,...,F_l)` and coordinate `x`, define

\[
\begin{array}{ll}
 f_F^1(x)=\min\{j:x\in F_j\},&
 \ell_F^1(x)=\max\{j:x\in F_j\},\\
 f_F^0(x)=\min\{j:x\notin F_j\},&
 \ell_F^0(x)=\max\{j:x\notin F_j\},                \tag{5.1}
\end{array}
\]

with the usual `infinity/-infinity` conventions.  Reversal transforms every
first/last pair by

\[
       (f,\ell)\longmapsto(|F|+1-\ell, |F|+1-f).    \tag{5.2}
\]

Choose a common retained endpoint pairing and linear openings of the old and
new owner cycles.  Split at the opening if it lies inside a retained path.
The two words are concatenations of the same common fragments in two induced
orders and orientations,

\[
 W_i=F_{\pi_i(1)}^{\epsilon_{i,1}}cdots
     F_{\pi_i(s)}^{\epsilon_{i,s}},qquad i=0,1.     \tag{5.3}
\]

Here `s=6` when the opening is between retained fragments and `s=7` when
one of the six retained paths is cut into two boundary pieces.  Put

\[
 o_{i,j}=\sum_{t<j}|F_{\pi_i(t)}|.                   \tag{5.4}
\]

Then the global first/last occurrence times are exactly

\[
 f_{W_i}^b(x)=\min_j\bigl(o_{i,j}+f_{F_{\pi_i(j)}^{\epsilon_{i,j}}}^b(x)\bigr),
\quad
 \ell_{W_i}^b(x)=\max_j\bigl(o_{i,j}+\ell_{F_{\pi_i(j)}^{\epsilon_{i,j}}}^b(x)\bigr)
                                                               \tag{5.5}
\]

for `b in {0,1}`.

### Theorem 5.1 (exact fragment-profile criterion)

For the supplied retained fragments and chosen topology:

1. `Sigma_vee(W_0)=Sigma_vee(W_1)` if and only if (5.5) agrees for every
   coordinate with `b=1`;
2. `Sigma_+-(W_0)=Sigma_+-(W_1)` if and only if (5.5) agrees for every
   coordinate with both `b=1` and `b=0`.

#### Proof

A coordinate belongs to the `j`th prefix union exactly when its first
occurrence is at most `j`, and it belongs to the `j`th suffix union exactly
when its last occurrence is at least `j`.  This proves the first statement.
Apply the same fact to coordinate absence, equivalently to complements, for
the second.  Formula (5.5) is the first/last occurrence rule for a
concatenation.  \(\square\)

Thus the actual six-path audit needs only each fragment length and the four
times (5.1) per coordinate, not all of its interval windows.

A stronger but convenient sufficient condition is **positionwise profile
matching**: after splitting at the opening, pair the old and new block
positions so that corresponding blocks have equal lengths and equal local
`Sigma_vee` (or local `Sigma_+-`) in their induced orientations.  Repeated
application of the one-slot replacement theorem then gives the desired
global signature.  This condition is not necessary; the exact weakest test
is (5.5).

## 6. Consequences and exact scope

The local result changes the upper-compression assessment in two ways.

1. The all-six ECO matching geometry has no union-signature obstruction.
   A constant-size, literal Johnson, OR-boundary-equivalent packet exists,
   and three such connector types also preserve the internal union and
   intersection coverage banks.
2. Simultaneous pointwise crossing-intersection transparency is impossible
   on the contracted alternating packet.  Any route which needs it must use
   nontrivial retained-path interiors, a larger buffer, or an independent
   lower/intersection certificate.

What is **not** proved is that the connector `M_*` is available in every
prepared Catalan forest, that replacing its existing retained paths by
(3.1) preserves the common cap/topology state, or that a positive-density
bank of such packets survives residence, router, compiler, and prescribed
task guards.  The explicit packet is a local catalogue atom.  Theorem 5.1
is the exact test for promoting a supplied real ECO occurrence.

## 7. Frozen audit

Run

```bash
python3 scratch/audit_independent_eco_sixseam_signature_connectors_20260731.py
```

It writes

```text
scratch/independent_eco_sixseam_signature_connectors_20260731.audit.json
```

and reports

```text
PASS_CONTRACTED_ECO_UNION_SIGNATURE_AND_TWOSIDED_NOGO
```

The script reconstructs the twelve symbolic owners, exhausts all `10,395`
perfect matchings, verifies every Hamilton cycle and every rotation/reversal,
checks both signatures, checks literal Johnson adjacency, and computes the
internal OR/AND banks of all six positive literal connectors.  It also
replays the first/last occurrence characterization independently.

Canonical JSON payload SHA-256:

```text
5a277da830c6fe163c25561134c67afb2ca86e22b00046f74daff93c45ad626c
```

Dependencies:

* `MATH_THEOREM_FULL_PREFIX_SUFFIX_SIGNATURE_UPPER_TRANSPARENCY_20260731.md`;
* `MATH_THEOREM_AD_REPAIRED_ECO_SIX_SEAM_RSB_EXPORT_AND_CUBE_GUARDS_20260731.md`.
