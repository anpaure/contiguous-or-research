# Audit of the exact `k=15` certificate and the general component-opening boundary theorem

Date: 2026-07-29

Status: **certificate PASS; general theorem proved with explicit one-core scope**.

## 1. Audit verdict

The canonical word

```text
answers/k15.word
```

has length `6438`, SHA-256

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b,
```

and its contiguous ORs contain all `32767` nonempty `15`-bit masks.  The
general deadline bound gives

\[
 r=8,\qquad W={15\choose8}=6435,\qquad
 \Lambda=\sum_{s=1}^7{15\choose s}=16383.
\]

For delay two the available short-interval count is

\[
 2W+{3\choose2}=12873<16383,
\]

whereas for delay three it is

\[
 3W+{4\choose2}=19311\ge16383.
\]

Thus `B(15)=W+3=6438`, and the literal word proves

\[
                         \boxed{\nu(15)=6438}.
\]

This equality does **not** depend on trusting CP-SAT, the quotient-factor
search, the seam census, or the compiler implementation.  Those objects give
reproducible provenance.  The proof trust boundary is only:

1. the proved deadline lower bound; and
2. direct deterministic enumeration of the literal word's interval ORs.

## 2. Independent end-to-end replay

The new standard-library-only auditor is

```text
scratch/audit_ad_k15_exact_6438_certificate_scope_20260729.py
```

with SHA-256

```text
0ea3eb504d0e5d6bce20f2ef6d98cab76625d5b4d347f90fd78ffd1a107e8cba.
```

Its retained output is

```text
scratch/ad_k15_exact_6438_certificate_scope_20260729.audit.json
```

with file SHA-256

```text
c1bb8a369fb05df7c9c59948df38cd1a6778355ffc95162dcceaa8f595a5e721
```

and internal semantic digest

```text
6f14769bbfa22e3a566046200ae664012fe385d6cef74ed5f2462dedb06c649b.
```

The auditor imports neither retained verifier.  It checks the following
chain from raw JSON and word bytes.

| object | SHA-256 |
|---|---|
| two-cycle factor | `0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555` |
| independent factor audit | `c5f700aef824b93e257957c313a7395eb3d2512c773e6d434f08934ba93ac6f4` |
| physical components | `f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151` |
| compiler audit | `5eeb04a61d8a085e89b05db9ca1075cfd64e5f95a9a35bcbb80711617579d125` |
| canonical word | `f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b` |

It reconstructs the two physical cycles of lengths `6390,45`, opens them at
cuts `22,41` with orientations `0,1`, and obtains the advertised middle path
with SHA-256

```text
bb453b77d4eb8d9b8199a3db9bec6d873367b23e9e1a8beb6a87b16a5ded4eb6.
```

The path seam has colour `17017` and symmetric difference two.  The deleted
cycle-edge colours are `18553,18033`; the seam recycles neither.  Direct
replay proves:

```text
word length                         6438
D^3 word length                     6435
D^3 word                            exact rank-eight layer
middle residence violations            0
fixed upper holes q=1,...,7             0
fixed lower holes                 (2,0,0,0,0,0,0)
the two q1 holes                 18033,18553
DA = DP                              true
word endpoints                  18553,18033
covered nonempty masks              32767
missing masks                           0
```

The root verifier `verify_word.py` (SHA-256
`7beea259577d243b8952634a39baef2c38d3dd5adb33649de1314b9975163b79`)
and the separately written verifier `scratch/verify_exact_or_word.py`
(SHA-256
`9d3498964c5b2eb83dcf6e36727e9b0e30cc2e17bac2db7ef057138cef1dd26d`)
also pass.  Their agreement is corroborating evidence; the new replay above
is an independent third implementation.

## 3. Exact scope of the one-seam census

There are two different catalogues and they must not be conflated.

### 3.1 The old recycling catalogue

The old `build_arcs` rule required the Johnson seam colour to equal exactly
one of the two deleted cut colours.  It has exactly `1290` residence-safe
directed seams.  Classifying by the first failed fixed upper depth gives

| first failed condition | seams |
|---|---:|
| upper `q=1` | 840 |
| upper `q=2` after passing `q=1` | 90 |
| upper `q=3` after passing `q=1,2` | 360 |
| pass all upper depths | 0 |

The unrestricted interval-union audit is stronger.  Its total upper-hole
histogram is

```text
one hole     390
two holes    570
three holes  330.
```

Hence every one of these `1290` fixed middle chronologies is genuinely
impossible at length `6438`.  This conclusion is not an artefact of using
minimum-width upper windows.

Indeed, if `D^d A=T`, every interval of `A` of length at least `d+1` is
exactly the union of the corresponding interval of `T`, while every shorter
interval is contained in a rank-`r` middle window.  Therefore the rank
greater than `r` interval spectra of `A` and `T` coincide.  An unrestricted
upper hole in `T` cannot be repaired by the lower compiler.

This is a no-go only for the `1290` recycling seams of the frozen two-cycle
factor.  It is not a no-go for all one-seam openings.

### 3.2 The complete Johnson and arbitrary endpoint catalogues

Removing the recycling equality gives `18000` cross-component Johnson
endpoint pairs and exactly `3960` residence-safe Johnson seams.  They split
as

```text
recycles exactly one cut colour     1290
recycles no cut colour              2670.
```

Exactly `60` nonrecycling seams are unrestricted-upper-complete.  Of those,
`30` have only the two lower-q1 holes and no lower-q2 hole; the other `30`
have one additional lower-q2 hole.  State `44 -> 12863` is in the first
class.

The still broader enumeration over every ordered pair of oriented openings,
including non-Johnson endpoint transitions, has

```text
directed pairs                       2300400
residence-safe pairs                   34740
unrestricted-upper-safe pairs            480
q1/q2 high-boundary candidates             60.
```

The last number is a high-boundary candidate count, not a proof that all 60
full compiler instances are feasible.  Only one positive instance is needed,
and its emitted literal word passes independently.  Thus the old recycled-
colour rule, rather than one-seam topology, was the decisive overconstraint.

## 4. General component-opening notation

Fix integers `r>=1`, `d>=1`, and let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a linear path of rank-`r` sets.  Write `D` for adjacent union and define
the maximal depth-`d` erosion

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i,
 \qquad 0\le p<W+d.                                      \tag{4.1}
\]

Assume that consecutive middle states are Johnson adjacent and every
internal positive coordinate run has length at least `d+1`.  Call such a
path `d`-resident.

Suppose `T` is obtained by cutting one edge in each of `c` cyclic components,
orienting and ordering the opened paths, and inserting `c-1` seams.  When
every component has length greater than an audited depth `q`, let

* `mu_q^-(S)` be the old cyclic multiplicity of the rank-`r-q` intersection
  target `S`;
* `L_{e,q}^-(S)` be the number of old `(q+1)`-windows labelled `S` which
  cross selected cut `e`; and
* `G_{a,q}^-(S)` be the number of new `(q+1)`-windows labelled `S` which
  cross selected seam `a`.

Then the opened-path multiplicity is exactly

\[
 m_q^-(S)=\mu_q^-(S)-\sum_{e\text{ cut}}L_{e,q}^-(S)
                         +\sum_{a\text{ seam}}G_{a,q}^-(S). \tag{4.2}
\]

The identical formula with intersections replaced by unions gives the fixed
upper ledger.  If a short component can lie wholly inside a `(q+1)`-window,
one must use the literal assembled chronology instead of (4.2); this is the
only locality qualification.

## 5. Erosion grading and endpoint capacity by depth

### Lemma 5.1 (exact boundary grading)

For a `d`-resident Johnson path, `D^dP=T` and

\[
 |P_p|=
 \begin{cases}
 r-p,&0\le p<d,\\
 r-d,&d\le p\le W-1,\\
 r-(W+d-1-p),&W\le p<W+d.
 \end{cases}                                               \tag{5.1}
\]

Thus there are exactly `2d` nonbulk source cells, with ranks

\[
 r,r-1,\ldots,r-d+1\quad\big|\quad
 r-d+1,\ldots,r-1,r.                                      \tag{5.2}
\]

**Proof.**  In any block of at most `d` Johnson transitions, the deleted
coordinates are distinct.  Repeating a deletion would require reinsertion
and a new internal positive run of length at most `d`, contrary to
residence.  Therefore each additional transition lowers the block
intersection rank by exactly one, proving (5.1).  Coordinatewise, a middle
one in an internal run belongs to some length-`d+1` subwindow contained in
that run.  If its run meets a global end, use instead the corresponding
truncated erosion window ending at that middle position (at the left) or
starting there (at the right).  In either case one erosion cell contributing
to the relevant `D^dP` entry contains the coordinate, while every
contributing erosion cell is a subset of that middle entry.  Hence
`D^dP=T`.  QED.

For `1<=q<=d`, define the nested boundary bank

\[
 B_q=\{0,\ldots,q-1\}\cup
     \{W+d-q,\ldots,W+d-1\},\qquad |B_q|=2q.                \tag{5.3}
\]

The `2d` total is therefore only the deepest aggregate capacity.  A
rank-`r-q` residual has raw access to at most the `2q` cells in `B_q`.

To make “residual” exact, put

\[
 \mathcal K^+(P)=\bigcup_{j=1}^{d-1}\operatorname{supp}(D^jP),
 \qquad
 \mathcal F(P)=
 \{S:1\le |S|<r,\ S\notin\mathcal K^+(P)\}.                \tag{5.4}
\]

Every member of `F(P)` must occur as a literal source letter in any one-core
antecedent: an interval of length `2,...,d` belongs to a fixed positive row,
and an interval of length at least `d+1` contains a rank-`r` middle window.

For `q<d`, put

\[
 \mathcal U_q=\mathcal F(P)\cap{[k]\choose r-q}.            \tag{5.5}
\]

For `q=d`, remove the rank-`r-d` targets already occurring in `P` and put

\[
 \mathcal U_d=
 \left(\mathcal F(P)\cap{[k]\choose r-d}\right)
 \setminus\operatorname{supp}(P).                          \tag{5.6}
\]

### Lemma 5.2 (nested endpoint-capacity theorem)

If `S in U_q` is represented by a one-core source letter `A_p subseteq P_p`,
then `p in B_q`.  Consequently, for every `1<=q<=d`,

\[
 \boxed{\sum_{s=1}^q|\mathcal U_s|\le2q}.                  \tag{5.7}
\]

**Proof.**  Outside `B_q`, equation (5.1) gives `|P_p|<r-q`, except for the
two cells of rank exactly `r-q` at boundary depth `q`.  Containment in an
equal-rank cell would force `S=P_p`.  For `q<d`, that cell also occurs in
the fixed row `D^(d-q)P`, contradicting `S in F(P)`.  For `q=d`, equality is
excluded explicitly by (5.6).  Hence every eligible position lies in
`B_q`.  The banks are nested and one source position cannot carry two
distinct targets, proving (5.7).  QED.

The inequalities (5.7) are necessary capacity tests, not sufficient ones.
Two targets may have the same sole endpoint, and assignments in adjacent
boundary cells may destroy a required adjacent union.

## 6. Exact Hall theorem

A boundary/core word is a sequence `C=(C_p)_(p=0)^(W+d-1)` satisfying

\[
 C_p\subseteq P_p,
 \qquad
 C_p\cup C_{p+1}=P_p\cup P_{p+1} \quad(0\le p<W+d-1).       \tag{6.1}
\]

For such `C`, define

\[
 N_C(S)=\{p:C_p\subseteq S\subseteq P_p\}.                 \tag{6.2}
\]

### Theorem 6.1 (exact one-core Hall criterion)

There exists a nonempty source word `A` with

\[
 DA=DP
\]

which covers every lower target as a contiguous interval if and only if
there is a core `C` satisfying (6.1) and

\[
 \boxed{\left|\bigcup_{S\in X}N_C(S)\right|\ge |X|
        \quad\text{for every }X\subseteq\mathcal F(P).}     \tag{6.3}
\]

Prescribed endpoint or boundary pins are enforced by fixing their matching
edges before applying (6.3) to the remaining targets and positions.

**Proof.**  Given `C` and a matching saturating `F(P)`, put `A_p=S` at the
position matched to `S`, and put `A_p=P_p` at every unmatched position.
Then

\[
 C\subseteq A\subseteq P,
\]

so (6.1) sandwiches every adjacent union and gives `DA=DP`.  The matched
letters supply all targets in `F(P)`; every other lower target already occurs
in a fixed positive derivative row.

Conversely, if `DA=DP`, then `A_p subseteq P_p`.  A target in `F(P)` cannot
be represented by an interval of length at least two, by the observation
after (5.4), so it has a distinct literal source position.  Taking `C=A`
gives (6.1), and those literal occurrences give a matching.  Hall's theorem
is exactly (6.3).  QED.

For boundary-forced targets, (6.3) restricts to

\[
 \left|\bigcup_{S\in X}(N_C(S)\cap B_q)\right|\ge|X|
 \quad
 (X\subseteq\mathcal U_1\cup\cdots\cup\mathcal U_q).       \tag{6.4}
\]

This is the requested exact endpoint Hall condition.  The scalar bounds
(5.7) are only its cardinality shadows.

## 7. The sharp lower-`q1` specialization

Assume now that the cyclic factor has an exact rainbow lower-q1 palette:
every rank-`r-1` colour occurs on exactly one factor edge.  Let `R` be the set
of the `c` cut colours and let `Q` be the set of rank-`r-1` Johnson seam
colours.  The opened path has exact q1 hole set

\[
                         H_1=R\setminus Q.                  \tag{7.1}
\]

In particular

\[
 |H_1|=c-|R\cap Q|.                                        \tag{7.2}
\]

Although the maximal erosion has `2d` boundary cells, a missing q1 colour
can use only the two outer endpoints.  The inner rank-`r-1` boundary cells
are retained path-edge colours; equality of ranks and the rainbow property
exclude a different missing colour.

Write `N=W+d`.  A rank-`r-1` colour `S` is left-endpoint legal exactly when

\[
 S\subseteq T_0,
 \qquad T_0\setminus T_1\subseteq S,                        \tag{7.3}
\]

and right-endpoint legal exactly when

\[
 S\subseteq T_{W-1},
 \qquad T_{W-1}\setminus T_{W-2}\subseteq S.                \tag{7.4}
\]

These are simply the equations

\[
 S\cup P_1=T_0,
 \qquad S\cup P_{N-2}=T_{W-1}.                              \tag{7.5}
\]

Therefore q1 absorption is possible with all other source cells maximal if
and only if the bipartite graph from `H_1` to `{L,R}` defined by (7.3)--(7.4)
has a matching saturating `H_1`.  In particular

\[
 \boxed{|H_1|\le2,\qquad |R\cap Q|\ge c-2.}                 \tag{7.6}
\]

Thus at least `c-2` distinct cut colours must be restored by the `c-1`
seams.  Count two is not sufficient: two holes both adjacent only to `L`
fail Hall.  If the two unrecycled colours belong to the components placed at
the global left and right ends, their endpoint eligibility is automatic from
rainbow uniqueness, and the two-endpoint matching succeeds.

For deeper lower shadows, let `H_q` be the hole set obtained from the exact
load formula (4.2), and retain only the genuinely boundary-forced part

\[
 \widehat H_q=H_q\cap\mathcal U_q.                           \tag{7.7}
\]

Then the exact quantitative consequence is

\[
 \boxed{\sum_{s=1}^q|\widehat H_s|\le2q
        \quad(1\le q\le d),}                               \tag{7.8}
\]

together with the full Hall cuts (6.4).  Targets already present in another
fixed derivative row are not counted in `widehat H_q`; calling every missing
minimum-width q-window a boundary demand would be an overcount.

## 8. Complete `c`-component opening theorem

### Theorem 8.1 (resident component-factor to optimal literal word)

Let a rank-`r` factor on all `W` middle sets be opened once in each of its
`c` components and concatenated into a `d`-resident Johnson path `T`.  Let
`P` be (4.1).  Within the exact one-core architecture `DA=DP`, an optimal
literal word of length `W+d` exists if and only if:

1. every rank greater than `r` target is the union of an interval of `T`;
2. there is a core `C` satisfying (6.1) and all Hall inequalities (6.3); and
3. every constructed source letter is nonempty.

If the original factor is q1-rainbow, condition 2 implies the sharper seam
condition (7.6) and the endpoint Hall test (7.3)--(7.4).

**Proof.**  Lemma 5.1 gives `D^dP=T`; (6.1)--(6.3) give a nonempty `A` with
`DA=DP`, hence `D^dA=T`, and cover every lower target.  The middle row covers
rank `r`.  If an upper target is `T_i union ... union T_j`, then it is
exactly

\[
 A_i\cup A_{i+1}\cup\cdots\cup A_{j+d},
\]

so item 1 supplies every upper target.  Conversely, for a universal one-core
word, upper-spectrum equality forces item 1 and Theorem 6.1 forces item 2.
QED.

The theorem is exact for the declared one-cut-per-component, resident
Johnson, maximal-erosion one-core architecture.  A negative result in this
architecture is not a global lower bound on arbitrary words.  A positive
literal word, as at `k=15`, is global.

The qualification `DA=DP` is material in other dimensions: an arbitrary
antecedent satisfying only `D^dA=T` need not be a one-core antecedent.  For
that larger class, the two-channel q1 obstruction remains valid by the
rank-`r-1` boundary-chain argument, but the deeper `2q` allocation and the
Hall equivalence above are not asserted.  The unrestricted exact replacement
is the full interval-witness Boolean system for `D^dA=T`, not a
fractional or rankwise Hall relaxation.  The canonical `k=15` word does
satisfy `DA=DP`, so this distinction does not weaken the certificate.

## 9. The `k=15` instance of the general theorem

Here `d=3`, so the total high boundary bank has ranks

```text
8,7,6 | 6,7,8
```

and nested raw capacities

```text
q=1: 2 endpoint cells
q=2: 4 endpoint cells
q=3: 6 endpoint cells.
```

The winning opening has `c=2`, restores no cut colour at its seam, and hence
has `|H_1|=2=c`.  This is allowed because `c-2=0`; the two colours pass the
opposite-endpoint Hall test.  There are no boundary-forced q2 targets.  The
full one-core family has `4945` targets: `4943` masks of ranks one through
five plus the two q1 colours.  Its exact compiler satisfies Hall and the
adjacent-union equations, and the emitted word supplies the literal PASS.

This explains both sides of the former paradox:

* every one of the `1290` one-colour-recycling seams really fails its fixed
  chronology; but
* recycling was never necessary, because the two global endpoint channels
  can absorb both cut colours when `c=2`.
