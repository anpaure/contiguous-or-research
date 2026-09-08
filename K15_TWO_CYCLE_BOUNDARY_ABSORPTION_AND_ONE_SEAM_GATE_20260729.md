# `k=15`: exact six-cell boundary absorption for the two-cycle factor

Date: 2026-07-29

Status: proved exact construction.  The retained two-cycle factor, broad
one-seam splice, boundary absorption, compiled word, and literal OR coverage
have all been independently replayed.

## 1. Audited input

The factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.best.json
```

has SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555.
```

Its independently rebuilt physical factor has two cycles of lengths `6390`
and `45`, all `6435` rank-eight vertices once, all `6435` rank-seven edge
colours once, cyclic minimum positive run four, and no depth-three residence
defect.  Both lower and upper fixed-window supports are complete for every
`q=1,...,7`.  Each component has vertex-union `[15]` and empty total
intersection.  The independently generated component file has SHA-256

```text
f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151.
```

Only opening, one seam, and the physical lower compiler remain.

## 2. Boundary grading

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad W=6435,
\]

be any depth-three-resident Johnson path obtained by opening and joining the
two cycles.  Its maximal depth-three erosion is

\[
 P_j=\bigcap_{\max(0,j-3)\le i\le\min(W-1,j)}T_i,
 \qquad 0\le j\le W+2.                         \tag{1}
\]

### Lemma 2.1 (exact erosion ranks)

The rank sequence of `P` is

\[
 8,7,6,\underbrace{5,\ldots,5}_{W-3\text{ entries}},6,7,8,   \tag{2}
\]

and `D^3P=T`.

**Proof.**  Write a Johnson transition as

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\]

In any three consecutive transitions, the deleted coordinates are distinct
and belong to the first state.  Repeating a deletion requires reinsertion
followed by deletion within three steps; deleting a coordinate inserted in
that three-step interval creates a positive run of length at most three.
Both contradict residence.  Thus four consecutive rank-eight states have
intersection rank `8-3=5`.  Truncating the intersection at the two global
ends gives ranks `8,7,6` and `6,7,8`.

Coordinatewise, a positive run internal to `T` has length at least four.
Therefore every occurrence of a coordinate in `T_i` belongs to at least one
of the four erosion letters whose union forms `T_i`; equivalently
`D^3P=T`.  \(\square\)

Put

\[
 \mathcal H=\{0,1,2,W,W+1,W+2\}.              \tag{3}
\]

These are exactly the six source positions whose erosion envelope has rank
at least six.

## 3. Which cut losses must use the six cells

Define the high residual family

\[
 \mathcal B(T)=
 \left(\binom{[15]}6\setminus\operatorname{supp}(DP)\right)
 \cup
 \left(\binom{[15]}7\setminus\operatorname{supp}(D^2P)\right). \tag{4}
\]

### Lemma 3.1 (high residuals are literal boundary targets)

Suppose `A<=P` and `DA=DP`.  If `A` realizes every rank-six and rank-seven
target, then every member of `B(T)` occurs as a literal source value `A_p`
at a distinct position `p in H`.

**Proof.**  Because `DA=DP`, every two-letter source union is a value of
`DP`, and every three-letter union is a value of `D^2P`.  An interval of at
least four source letters contains a four-letter window, hence contains a
rank-eight value of `T` and cannot have rank six or seven.  Thus a target in
(4), absent from the two fixed derivative rows, can occur only as a
one-letter interval.

Every antecedent satisfies `A_p subseteq P_p`.  By (2), an internal `P_p`
has rank five, so a rank-six or rank-seven literal can occur only at a
position in (3).  Distinct targets require distinct source positions.
\(\square\)

In particular

\[
 |\mathcal B(T)|\le6                                      \tag{5}
\]

is necessary, but it is not sufficient: adjacent boundary pins can omit the
same forced coordinate.

## 4. Exact six-cell absorption theorem

For an injection

\[
 \phi:\mathcal B(T)\longrightarrow\mathcal H,
\]

define a partially pinned word

\[
 A^\phi_p=
 \begin{cases}
 S,&\phi(S)=p,\\
 P_p,&p\notin\phi(\mathcal B(T)).
 \end{cases}                                                \tag{6}
\]

### Theorem 4.1 (necessary and sufficient boundary absorption)

The high residual family can be installed as distinct literal source
letters while leaving every unpinned source position maximal and preserving
`DA=DP` if and only if there is an injection `phi` such that

\[
 S\subseteq P_{\phi(S)}                                    \tag{7}
\]

for every `S in B(T)`, and

\[
 A^\phi_p\cup A^\phi_{p+1}=P_p\cup P_{p+1}
 \qquad(0\le p<W+2).                                      \tag{8}
\]

**Proof.**  Necessity follows from `A<=P`, distinct literal ownership, and
`DA=DP`.  Conversely, (7) gives `A^phi<=P`, and (8) is exactly
`DA^phi=DP`.  Hence (6) is the required partial antecedent.  \(\square\)

The theorem has a direct 0--1 formulation.  Introduce `y_(S,p)` only when
`S subseteq P_p`, with

\[
 \sum_{p\in\mathcal H}y_{S,p}=1,
 \qquad
 \sum_{S\in\mathcal B(T)}y_{S,p}\le1.                     \tag{9}
\]

For a coordinate `x`, put

\[
 \epsilon_{p,x}=
 \mathbf1_{x\notin P_p}
 +\mathbf1_{x\in P_p}
   \sum_{\substack{S\in\mathcal B(T)\\x\notin S}}y_{S,p}. \tag{10}
\]

Then (8) is equivalent to the omission rows

\[
 \epsilon_{p,x}+\epsilon_{p+1,x}\le1
 \quad
 \left(x\in P_p\cup P_{p+1}\right).                       \tag{11}
\]

Indeed, the left side counts whether each endpoint of the positive edge
omits `x`; their union contains `x` exactly when the count is at most one.
Equations (9)--(11) are therefore an exact boundary CSP, not a marginal
Hall relaxation.

## 5. Local form at one end

At the left end write

\[
 P_1=P_0\setminus\{a\},\qquad
 P_2=P_1\setminus\{b\},\qquad
 P_3=P_2\setminus\{c\}.                                    \tag{12}
\]

A rank-seven facet `S=P_0\setminus\{x\}` is legal at position zero exactly
when

\[
 x\ne a.                                                    \tag{13}
\]

If simultaneously a rank-six facet
`U=P_1\setminus\{y\}` is placed at position one, then the two pins preserve
both adjacent unions exactly when

\[
 y\ne b,qquad y\ne x.                                     \tag{14}
\]

The first inequality in (14) is `U union P_2=P_1`; the second is
`S union U=P_0`.  A rank-six target placed directly at position zero must
contain `a`.  The right endpoint has the reversed identical rules.  These
are the explicit collar conflicts hidden by a containment-only boundary
matching.

## 6. The q1 colour is automatic for two cycles

Let the two deleted cut colours be `c_1,c_2`, and let the Johnson seam colour
be `s`.  The natural middle q1 hole set is

\[
 H_1=\{c_1,c_2\}\setminus\{s\}.                            \tag{15}
\]

Place the first component's deleted colour at the left extreme source cell
and the second component's deleted colour at the right extreme source cell,
whenever each is in `H_1`.  This always satisfies (13): at an endpoint the
deleted cut facet and the retained incident-edge facet are distinct because
the factor's rank-seven edge deck is globally squarefree.  Therefore the
coordinate omitted by the retained facet belongs to the cut facet.

Consequently the q1 boundary SDR is automatic for **every** residence-safe
Johnson seam:

* if `s` equals one cut colour, the other cut colour uses its own outer
  endpoint;
* if `s` equals neither, both cut colours use opposite outer endpoints.

Thus a search restriction requiring the seam colour to equal an incident
cut colour is sound but unnecessary.

## 7. Coupling to the complete compiler

The full residual family is

\[
 \mathcal F(T)=
 \bigcup_{j=1}^{5}\binom{[15]}j\ \cup\ \mathcal B(T).       \tag{16}
\]

Use assignment variables `m_(S,p)` for `S in F(T)`, `S subseteq P_p`, with
one position per target and at most one target per position.  Replace
`B(T)` by all of `F(T)` in (10)--(11).  These are exactly the adjacent
omission rows

\[
 A_p\cup A_{p+1}=P_p\cup P_{p+1}.                           \tag{17}
\]

If the resulting integral system is feasible, set unmatched source letters
to their maximal values `P_p`.  Then `A<=P`, `DA=DP`, and `D^3A=T`; every
target in (16) is literal, ranks six and seven outside (16) occur in the
fixed derivative rows, and all upper witnesses of `T` lift to contiguous
source intervals.  The final independent literal OR verifier is still
required.

Therefore Theorem 4.1 is the exact compiler-side boundary absorption gate;
it is a necessary high-rank projection of the full physical compiler and a
sufficient partial extension with all other cells maximal.  Passing mere
containment Hall at the six cells is not enough, while scalar slack `2928`
does not enter the criterion.

## 8. Exact broad-seam certificate

The full residence-safe Johnson seam catalogue between the two opened
components has the following exact census:

```text
oriented cross-component Johnson arcs       18000
depth-three-residence-safe arcs               3960
all-fixed-upper and natural-lower-q2 safe       60
```

The first surviving arc in deterministic state order compiles.  Its literal
data are

```text
component order        0,1
component lengths      6390,45
cuts                    22,41
orientations            forward,reverse
deleted cut colours     18553,18033
new seam colour         17017
```

The seam colour is different from both deleted colours.  Thus this
certificate lies outside the old incident-colour recycling catalogue.  Its
middle chronology has exact shadow ledger

```text
lower holes by q        2,0,0,0,0,0,0
upper holes by q        0,0,0,0,0,0,0
residence violations    0
```

The two rank-seven holes are exactly `18553` and `18033`.  The six-cell
system (9)--(11) assigns them to source positions `0` and `6437`,
respectively.  There are no rank-six residuals.  The complete compiler then
has

```text
base rank-at-most-five targets             4943
boundary residual targets                     2
ordinary physical matching                4945/4945
adaptive one-core assignment              4945/4945
adjacent omission rows                        38628
```

and produces a word of length `6438` satisfying `DA=DP` and `D^3A=T`.
Independent literal interval enumeration gives

```text
covered nonempty masks                     32767/32767
enumerated intervals before full union       122031
middle rank-eight row                       6435/6435
missing masks                                      0
```

The word SHA-256 is

```text
9ad115dc180b01b3bc0717c2ad37729d3e0e1920874a1f656df8d2e6e93340ef.
```

Authoritative artifacts are

```text
scratch/k15_from3_two_cycle_broad_seam_20260729/
    threadH_broad_seam.word
    threadH_broad_seam.audit.json
    threadH_broad_seam.independent.audit.json
    threadH_broad_seam.reconstruction.audit.json
scratch/threadH_from3_two_cycle_broad_seam_search_20260729.py
scratch/audit_k15_from3_two_cycle_broad_seam_certificate_20260729.py
```

Their SHA-256 values, in the same order after the word, are

```text
05f030de4b034fd9ead48d2bd150055fdce1bd451d145617fa6234e26b27c331
e94825ee60230932d04efe4d04fa3bcc9b04d4185ce2ed8ce6c57621e3ab8980
0d9076d74c355c5305f7843fd4d2356cde91904607202b17869162869a6e5816
524f709e570e3f44c118491d7307ad7f838e5bed05f99acf5f90280bd47076b0
2f5672b58980bcb7bcd53d390118dde3f0f9d267692c82c91c9d737234f1106c
```

The universal monotone-deadline lower bound gives

\[
 \nu(15)\ge B(15)=\binom{15}{8}+3=6438.
\]

The verified word gives the reverse inequality.  Therefore

\[
 \boxed{\nu(15)=B(15)=6438}.                              \tag{18}
\]
