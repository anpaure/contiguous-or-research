# Exact negative-window compiler and suffix-aware Benders oracle at `k=15`

Date: 2026-07-29  
Lane: AD  
Status: theorem-level code/mathematics audit; no solve was run

## 1. Scope and verdict

This note audits

```text
scratch/optimize_k15_exact_compiler_maxcoverage.py
```

and derives the exact extension needed for a joint carrier/common-compiler
search at total length at most `6457`, with `6438` as the terminal case.
The audited source implements an exact fixed-carrier **prefix** maximum-
coverage problem.  It does not implement the exact length objective once a
suffix is allowed: residual masks can share suffix intervals, and intervals
crossing the prefix/suffix seam can matter.

There is nevertheless an exact extension with a small physical interval
family.  For suffix length `s`, use
the usual `19,311` short prefix intervals and add only

\[
                       \frac{s(s+7)}2
\]

intervals ending in the suffix.  At `s=19` this is only `247` additional
physical intervals.  Assign every lower target to one of these intervals and
apply one common negative-window closure to the prefix and suffix together.
The resulting Boolean model is equivalent to existence of a literal word of
length `6438+s` in the **fixed first-6438, upper-perfect middle-prefix**
architecture.  In particular, `s=19` is an exact test of length at most
`6457` inside that declared architecture, and `s=0` is its exact `6438` test.
No normalization theorem puts every arbitrary length-6457 word in this
class.

The source-incidence variables are deterministic once the interval assignment
is fixed.  They can therefore be removed from that representation and
separated by three exact families of cover no-goods: positive-target,
middle-witness, and nonempty-letter cuts.  A smaller-start practical
alternative keeps only the literal letter incidences and lazily adds exact OR
occurrence rows for verifier-missing targets.  Both are complete CEGAR
oracles, not relaxations.  Outer Hall is useful presolve only and must not be
optimized as a surrogate objective.

## 2. Frozen notation and audited source semantics

Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad
 W=\binom{15}{8}=6435,\qquad B=W+d=6438.
\]

Let

\[
 \mathcal L=\{X\subseteq[15]:1\le |X|\le7\},
 \qquad |\mathcal L|=16383.
\]

For a fixed middle carrier

\[
                    T=(T_0,\ldots,T_{W-1}),
\]

the maximal linear antecedent is

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i,
       \qquad 0\le p<B.                                  \tag{2.1}
\]

The audited source builds exactly the following prefix model.

* Its physical cells are the intervals of lengths `1,2,3` in `[0,B-1]`,
  hence

  \[
                         B+(B-1)+(B-2)=19311.             \tag{2.2}
  \]

* A selector `y_(X,I)` assigns lower target `X` to cell `I`.  Selectors have
  target and cell capacity one.
* A source incidence `z_(p,x)` exists exactly when `x in P_p`.
* If a selected cell `I` is labelled `X`, it blocks `(p,x)` precisely when
  `p in I` and `x notin X`.
* Lines implementing

  ```text
  z + blocker <= 1
  z + sum(blockers) >= 1
  ```

  make `z_(p,x)` equivalent to the statement that no selected negative
  window blocks `(p,x)`.
* Conditional positive-bit clauses force `OR_(p in I) A_p=X` on every
  selected interval; unconditional clauses force `D^3 A=T` and every source
  letter to be nonempty.

The individually feasible edge filter in the imported `build_graph` is also
exact.  For

\[
 C_{i,x}=\{p\in[i,i+3]:x\in P_p\},                       \tag{2.3}
\]

an isolated assignment `(X,I)` is possible if and only if

\[
 X\subseteq\bigcup_{p\in I}P_p,                          \tag{2.4}
\]

\[
 P_p\cap X\ne\varnothing\quad(p\in I),                  \tag{2.5}
\]

and

\[
 C_{i,x}\subseteq I,\ x\in T_i\quad\Longrightarrow\quad x\in X.
                                                               \tag{2.6}
\]

Indeed, (2.4) supplies every positive target coordinate, (2.5) prevents an
empty letter after the isolated negative window, and (2.6) prevents that
window from deleting every possible witness of a required middle coordinate.
They are necessary for the same reasons.  The code's `mandatory` dictionary
is exactly (2.6), grouped by equal carrier sets `C_(i,x)`.

### Theorem 2.1 (the audited objective is exact prefix coverage)

For fixed `T`, the optimum of the audited model equals the maximum number of
lower targets simultaneously covered by a nonempty prefix word `A` satisfying
`A_p subseteq P_p` and `D^3 A=T`.

#### Proof

Every selected interval is an actual target occurrence, so the objective is
at most actual lower coverage.  Conversely, take any such word and choose one
actual occurrence for each lower target it covers.  A lower occurrence wholly
inside the prefix has length at most three: any four consecutive prefix
letters have union `T_i`, of rank eight.  Occurrences belonging to different
targets are distinct intervals.  The chosen intervals satisfy (2.4)--(2.6).
Their common maximal negative-window closure contains the original word,
because an actual interval labelled `X` cannot contain a coordinate outside
`X`.  It therefore retains all selected target witnesses, all middle
witnesses, and nonempty letters, and is feasible in the audited model with
objective equal to the original word's lower coverage.  \(\square\)

Thus “explicitly assigned” versus “accidentally covered” is harmless at an
optimal solution, although the two counts may differ at an intermediate
incumbent.

## 3. Exact suffix-aware interval family

Fix `s>=0`, put `L=B+s`, and extend the envelope by

\[
 E_p=\begin{cases}
 P_p,&0\le p<B,\\
 [15],&B\le p<L.
 \end{cases}                                             \tag{3.1}
\]

Define `I_s` to contain

1. every interval `[a,b] subseteq [0,B-1]` of length at most three; and
2. every interval `[a,b]` with `b>=B` and `a>=B-3`.

### Lemma 3.1 (no other lower interval is possible)

If `A_p subseteq E_p`, `D^3(A_0,...,A_(B-1))=T`, and an interval of `A`
has OR of rank at most seven, then that interval belongs to `I_s`.

#### Proof

An interval wholly in the prefix and of length at least four contains four
consecutive positions `[a,a+3]`, whose union is `T_a` and has rank eight.  An
interval ending in the suffix but starting at `a<=B-4` contains the same
four-position prefix block.  OR is monotone, so neither interval can have
rank at most seven.  The remaining possibilities are exactly `I_s`.
\(\square\)

The number of suffix-ending intervals is

\[
 \sum_{t=0}^{s-1}(t+4)=\frac{s(s+7)}2.                  \tag{3.2}
\]

Hence

\[
 |\mathcal I_{19}|=19311+247=19558,
 \qquad |\mathcal I_0|=19311.                           \tag{3.3}
\]

It is unsound to restrict suffix-ending witnesses to length at most three;
their exact maximum length is `s+3`.

## 4. Exact fixed-carrier model for total length `B+s`

For `I in I_s`, define

\[
 C_{i,x}=\{p\in[i,i+3]:x\in E_p\};                      \tag{4.1}
\]

these sets lie wholly in the prefix.  Retain an edge `e=(X,I)` exactly when

\[
 X\subseteq\bigcup_{p\in I}E_p,                         \tag{4.2}
\]

\[
 E_p\cap X\ne\varnothing\quad(p\in I),                 \tag{4.3}
\]

and

\[
 C_{i,x}\subseteq I,\ x\in T_i\quad\Longrightarrow\quad x\in X.
                                                               \tag{4.4}
\]

For suffix-ending intervals, (4.2) is automatic because the interval
contains a suffix position with envelope `[15]`; (4.3) is automatic at the
suffix positions and must only be checked on the at most three prefix-tail
positions.  Condition (4.4) should be computed by scanning the middle
carrier sets `C_(i,x)` and testing interval containment.  One must **not**
generalize the current short-cell implementation by enumerating all subsets
of a suffix-ending interval: at `s=19` such an interval may have length 22,
and that exponential enumeration is unnecessary.

Eligibility also has an exact compact structure.  Every suffix-only interval
`B<=a<=b<L` is individually eligible for every nonempty lower target.  For a
crossing interval with `a in {B-3,B-2,B-1}`, eligibility depends on `a` and
`X` but not on the suffix endpoint `b`: all conditions inspect only the
fixed prefix portion `[a,B-1]`.  Thus the at most
`16383*247=4,046,601` raw tail edge incidences need not be expanded merely to
build domains; suffix-only choices and the endpoint ranges of an admissible
crossing start can be stored compactly.

Use one Boolean `y_e` per retained edge and one Boolean `z_(p,x)` per
`x in E_p`.  Write

\[
 \mathcal B_{p,x}=\{(X,I):p\in I,\ x\notin X\}.          \tag{4.5}
\]

The exact model is:

\[
 \sum_{I:(X,I)\text{ retained}}y_{X,I}=1
       \qquad(X\in\mathcal L),                           \tag{4.6}
\]

\[
 \sum_{X:(X,I)\text{ retained}}y_{X,I}\le1
       \qquad(I\in\mathcal I_s),                        \tag{4.7}
\]

\[
 z_{p,x}+y_e\le1
       \qquad(e\in\mathcal B_{p,x}),                    \tag{4.8}
\]

\[
 z_{p,x}+\sum_{e\in\mathcal B_{p,x}}y_e\ge1,            \tag{4.9}
\]

\[
 \sum_{p\in I:x\in E_p}z_{p,x}\ge y_{X,I}
       \qquad((X,I)\text{ retained},\ x\in X),          \tag{4.10}
\]

\[
 \sum_{p\in[i,i+3]:x\in E_p}z_{p,x}\ge1
       \qquad(i<W,\ x\in T_i),                          \tag{4.11}
\]

and

\[
 \sum_{x\in E_p}z_{p,x}\ge1\qquad(0\le p<L).           \tag{4.12}
\]

Equations (4.8)--(4.9) make `z` the entrywise-maximal common word; `z` is not
a discretionary second compiler.

### Theorem 4.1 (exact common-prefix architecture)

Assume `T` is a rank-eight deck and its unrestricted upper rows cover every
rank-nine-through-fifteen mask.  Model (4.6)--(4.12) is feasible if and only
if there exists a nonempty literal word of length `B+s` whose first `B`
letters have third OR derivative `T` and which covers every nonempty mask.

#### Proof

Suppose first that such a word `A` exists.  Choose one occurrence interval
for every lower target.  By Lemma 3.1 all chosen intervals lie in `I_s`, and
distinct targets use distinct intervals.  Conditions (4.2)--(4.4) follow
from the actual occurrence, nonempty letters, and `D^3A=T`.  Define `z` by
the common maximal closure of all chosen negative windows.  The original
word is contained entrywise in this closure: no chosen interval labelled
`X` contains an original occurrence of a coordinate outside `X`.  Therefore
all positive target witnesses, middle witnesses, and nonempty letters
survive, proving (4.6)--(4.12).

Conversely, (4.8)--(4.9) say that each selected interval contains no
coordinate outside its label, while (4.10) supplies every coordinate inside
the label.  Hence every lower target occurs literally.  Equations
(4.11)--(4.12), together with `z subseteq E`, give `D^3A=T` and nonempty
letters.  The middle deck covers rank eight.  More generally, for
`0<=a<=b<W`,

\[
 \bigvee_{p=a}^{b+3}A_p=\bigvee_{i=a}^{b}T_i.           \tag{4.13}
\]

Thus every arbitrary-length noncrossing upper witness of the certified
carrier lifts to a literal prefix witness; every higher rank is covered and
the word is universal.  \(\square\)

A word shorter than `B+s` in the same architecture can be padded on the
right by a nonempty full-set letter without losing any occurrence or
changing the first `B` letters.  Therefore feasibility at `s=19` is exactly
the question “length at most `6457`” within the upper-perfect fixed-prefix
architecture, while `s=0` is its exact length-`6438` question.

For the audited H19 carrier, the prefix has `32,202` supported incidences.
At `s=19`, (3.1) adds exactly `15*19=285`, for `32,487` `z` variables before
any deterministic elimination.

## 5. Two complete exact compiler CEGAR formulations

The `z` variables are uniquely determined by `y`.  Thus one exact projected
master exposes only interval assignments; the following finite cut families
are an exact separation oracle.  No information-theoretic or encoded-size
minimality claim is made.

A compact state representation gives each target one integer variable

\[
              \phi_X\in\{I:(X,I)\text{ is retained}\},  \tag{5.0}
\]

and may impose one global `AllDifferent(phi_X : X in L)`.  This uses exactly
`16,383` explicit assignment variables, independently of the edge count,
although a CP implementation may internally create equality literals.  The
unary literal `y_(X,I)` below means the equality literal `[phi_X=I]`; every cut in
this section can be emitted directly as a disjunction of disequalities, so
neither unary selectors nor source incidences need be materialized in the
initial master.  `AllDifferent` is redundant for exactness: if distinct
targets `X,Y` chose the same interval, a coordinate of their symmetric
difference would be simultaneously forbidden by one label and required by
the other's positive-target cut.  It remains useful propagation.

For coordinate `x`, an edge `f=(Y,J)` covers position `p` negatively when

\[
                         p\in J,\qquad x\notin Y.         \tag{5.1}
\]

### Positive-target cuts

For `e=(X,I)`, `x in X`, let

\[
 U_{e,x}=\{p\in I:x\in E_p\}.                           \tag{5.2}
\]

For every edge set `F` whose negative `x`-windows cover `U_(e,x)`, add

\[
                       y_e+\sum_{f\in F}y_f\le |F|.      \tag{5.3}
\]

### Middle-witness cuts

For `i<W`, `x in T_i`, and every edge set `F` whose negative `x`-windows
cover `C_(i,x)`, add

\[
                            \sum_{f\in F}y_f\le |F|-1.   \tag{5.4}
\]

### Nonempty-letter cuts

For a position `p`, say that `f=(Y,J)` covers coordinate `x in E_p` when
`p in J` and `x notin Y`.  For every `F` covering all of `E_p`, add

\[
                            \sum_{f\in F}y_f\le |F|-1.   \tag{5.5}
\]

### Theorem 5.1 (cut completeness)

Equations (4.6)--(4.7) together with all cuts (5.3)--(5.5) are equivalent to
the extended model (4.6)--(4.12).

#### Proof

Every cut is sound: selecting all listed blockers deletes every possible
witness in (5.3) or (5.4), or every coordinate of the letter in (5.5).
Conversely, reconstruct `z` deterministically from a proposed integral `y`.
If a selected target coordinate is absent, its selected blockers cover
`U_(e,x)` and violate (5.3).  If a middle coordinate is absent, its blockers
cover `C_(i,x)` and violate (5.4).  If a letter is empty, its blockers cover
`E_p` and violate (5.5).  If none occurs, the reconstructed `z` satisfies
(4.8)--(4.12).  \(\square\)

An implementation need not enumerate these exponential families.  Given an
integral assignment, reconstruct `z` in time linear in the selected-window
incidences.  On failure, delete redundant selected blockers greedily until
an inclusion-minimal cover remains and emit the corresponding no-good.
Finite termination is immediate because every rejected integral assignment
receives a violated valid cut.

In the integer representation, a target failure cut is literally

\[
 [\phi_X\ne I]\ \lor\!
       \bigvee_{(Y,J)\in F}[\phi_Y\ne J],                \tag{5.7}
\]

and the middle/nonempty cuts omit the first literal.  Thus the separator
returns ordinary forbidden partial assignments; it needs no linearization
until the solver API requests one.

### Smaller-start literal-word CEGAR

For search, the smaller-start audited state is usually the direct word
formulation.  Keep only Boolean incidences `a_(p,x)` for `x in E_p`, impose

\[
 \bigvee_{p=i}^{i+3}a_{p,x}\quad(i<W,\ x\in T_i),
 \qquad
 \bigvee_{x\in E_p}a_{p,x}\quad(p<L),                  \tag{5.7a}
\]

and decode the current literal word.  If a lower target `X` is missing, add
one exact occurrence block

\[
 \bigvee_{I\in\mathcal I_s(X)}w_{X,I},                 \tag{5.7b}
\]

where `I_s(X)` contains the eligible intervals from (4.2)--(4.4), and
`w_(X,I)` implies

\[
 a_{p,x}=0\quad(p\in I,\ x\notin X),
 \qquad
 \bigvee_{p\in I}a_{p,x}\qquad(x\in X).                \tag{5.7c}
\]

These implications say literally `OR_(p in I) A_p=X`.  Thus (5.7b) is
necessary for every universal word and sufficient for target `X`.  Adding it
only after direct verification finds `X` missing is exact CEGAR; a universal
word extends every accumulated relaxation, and zero verifier misses is a
literal certificate.  At the H19 envelope and `s=19`, this starts with only
`32,202+15*19=32,487` word incidences.  The interval-assignment closure and
this direct-word formulation have the same final feasibility set by Theorem
4.1; neither representation is claimed absolutely minimal.

Pairwise conflicts arise from `|F|=1` in (5.3), or `|F|=2` in (5.4)--(5.5);
the `|F|=1` middle/nonempty cases are unary exclusions.
Hall inequalities

\[
 \sum_{X\in S}\sum_I y_{X,I}\le |N(S)|                 \tag{5.6}
\]

are valid presolve consequences of interval capacity, but they do not imply
any of the common-word cuts above.

Two useful exact presolve consequences deserve to be materialized.

1. **Nested-interval monotonicity.**  If `I subseteq J`, an interval labelled
   `X` and the larger interval labelled `Y` require `X subseteq Y`.  Hence

   \[
      I\subseteq J,\ X\not\subseteq Y
      \quad\Longrightarrow\quad y_{X,I}+y_{Y,J}\le1.    \tag{5.8}
   \]

   This is a two-edge instance of (5.3): any `x in X-Y` is blocked on all of
   `I` by `(Y,J)`.

2. **Suffix antichain capacity.**  For `s>=1`, the suffix-ending intervals
   have exactly `s+3` possible start positions, namely `B-3,...,L-1`.  For one fixed
   start, interval ORs are nested as the endpoint moves right.  Therefore,
   for every inclusion antichain `A subseteq L`,

   \[
     \sum_{X\in\mathcal A}
       [\phi_X\text{ is suffix-ending}]\le s+3.          \tag{5.9}
   \]

   This is not an outer-Hall heuristic; it is an exact consequence of
   literal OR chronology.  Domain-specific Hall cuts between antichain
   targets and their admissible suffix start positions strengthen (5.9)
   further without changing the feasible set.  For `s=0` the left side is
   identically zero.  At `s=19`, each fixed-rank lower layer is an antichain,
   so at most 22 targets of that rank can be assigned to suffix-ending
   intervals.

## 6. Sound carrier-level Benders use

The H19 carrier audited below is a linear braid path: its endpoint masks have
Hamming distance eight, and its JSON has no quotient choices, directed arcs,
or voltage.  It is therefore a fixed-carrier regression, not an incumbent of
the quotient Benders master described next.

For a future strict-equivariant master, let `a_e` select a directed quotient
arc.  The smallest exact skeleton derived in this audit for the architecture
uses only:

1. one directed Hamilton circuit on the `N=429` middle orbits;
2. unit voltage, so its physical lift is one rank-eight deck cycle; and
3. one opening variable `c_u` choosing the canonical physical representative
   of quotient middle vertex `u` as the first carrier state.

The frozen k15 catalogue has 23,996 directed arcs.  With two voltage integers
and 429 opening bits, this skeleton has 24,427 explicit variables before lazy
cuts.  It needs no 11,998 undirected-choice variables, lower-shadow blocks, or
Hall flow: those are optional propagation or additional ansatz restrictions,
not part of literal compiler exactness.

Residence, first-shadow rainbows, Hall, or carrier-side lower shadows may be
added as presolve/design restrictions, but none is part of the common-word
equivalence proved here.  In particular, outer Hall must not be the objective.

The corrected accumulated-union automaton is the only valid carrier-side
upper oracle; no fixed-`q` replacement is allowed.  Its use depends on `s`:

* At `s=0`, upper carrier coverage is necessary.  Any source interval of at
  most three positions is contained in some four-position middle window and
  has rank at most eight; every longer prefix interval obeys (4.13).  Hence a
  missing noncrossing carrier-upper target makes that opening infeasible.
* At `s>0`, an interval touching the suffix can repair an upper carrier hole.
  In the broad strict-carrier-prefix model, the automaton may certify targets
  already covered by the prefix, but its failure is **not** a valid carrier
  cut: send that target to a whole-word occurrence automaton instead.  The
  lower interval family `I_s` is not valid for this purpose.  For an upper
  target `U`, let `g_p` mean `A_p subseteq U` and, for `x in U`, use the exact
  reset recurrence

  \[
   h_{p,x}=g_p\wedge(a_{p,x}\vee h_{p-1,x}),\qquad h_{-1,x}=0. \tag{6.0}
  \]

  Then `OR_p AND_(x in U) h_(p,x)` is equivalent to one whole-word interval
  with OR `U`: take the clean run since the last position with `g=0`.
  Instantiate this only for verifier-missing high targets.  If the master
  deliberately declares the upper-perfect subclass of Theorem 4.1, then
  unrestricted-upper cuts remain valid by definition and (6.0) is unnecessary.

For an integral directed carrier and opening, linearize `T`, compute `P`, and
solve either exact compiler oracle in Section 5.  A passing oracle is decoded
and exhaustively verified.  An `INFEASIBLE` oracle result gives the universally
sound pair no-good

\[
 c_{u^*}+\sum_{e\in C^*}a_e\le429,                     \tag{6.1}
\]

where `C*` is the incumbent set of 429 directed quotient arcs and `u*` the
opening.  `UNKNOWN`, timeout, one failed compiler heuristic, or one Hall shore
gives no cut.  The guard must be directed at `s>0`: reversal moves a right
suffix to the left and is not the same architecture.

Unit voltage gives `T_(i+N)=rho^v(T_i)`.  Cuts separated by `N` physical
positions are therefore related by a coordinate permutation; permuting every
compiler/suffix letter and every target proves that the `W=6435` physical
openings have exactly `N=429` feasibility classes.  Thus (6.1) excludes one
class without discarding the same carrier at another opening.  After all 429
classes are conclusively infeasible, the whole directed carrier may be
excluded.

A smaller compiler-core cut is valid only after separately proving that the
full joint subproblem remains infeasible when merely that directed core is
fixed.  A fixed-carrier UNSAT core cannot be lifted unguarded: changing a zero
envelope bit can create a witness, changing a middle obligation changes the
closure, and changing the opening changes every boundary cell.

This is finite and exact within the declared strict-equivariant
carrier-prefix architecture.  It is not a global impossibility model for all
length-6457 words: positive deadline slack does not normalize every word to a
flat cyclic carrier prefix.

## 7. Thresholds and exact scope of the present artifacts

The stored H19 prefix solve reports

\[
 \text{outer matching}=16364,
 \qquad \text{common-prefix optimum}=16362.              \tag{7.1}
\]

Thus the outer graph has deficiency `19`, but one common prefix has minimum
deficiency `21`.  This is a concrete counterexample to using outer Hall as
the objective proxy.

Appending every residual mask separately turns a prefix with `h` holes into
a word of length `6438+h`, but this is only a sufficient completion.  The
stored 21-hole prefix has a 20-letter suffix because

\[
                         9524\lor13616=13620.             \tag{7.2}
\]

Consequently none of the following implications is sound:

* outer deficiency at most `19` implies a length-`6457` word;
* prefix hole count at most `19` is necessary for length `6457`; or
* maximizing prefix coverage minimizes the exact completion length.

The exact `s=19` model in Section 4 decides the upper-perfect carrier-prefix
question without any of these proxies.  The independently audited outer Hall
deficiency already excludes `s=0` for this fixed H19 carrier; the reported
common-prefix optimum sharpens its fixed-carrier deficit from `19` to `21`
but is not needed for that impossibility.  Neither statement decides the
suffix-aware `s=19` model.

## 8. First concrete regression: the 34-mask suffix master

The user-launched regression is

```text
scratch/solve_k15_exact_compiler_with_suffix.py
scratch/k15_exact_compiler_residual_pool_union34.json.
```

The current synchronized local/H100 source has SHA-256

```text
163f09fe31bf0afdc22ed5022c863bed9e817516726f8c6d07286a35d71e84ec.
```

The already-running pool-34 process was launched from the earlier SHA-256

```text
2d5ed36849042d56be2397a8137933554f3c1b6ced12a9e1b3ded2fa5d26c6ec.
```

Its frozen `MODEL_BUILT` row records 190 suffix-only intervals and 6,460
witnesses, so it is the suffix-only regression audited below even though the
file on disk was later replaced.  The current source adds 57 crossing
intervals and, when `--hint-word` is supplied, clears/replaces inherited
hints; it is audited separately after
Proposition 8.2.  The pool hash is

```text
4fbddba352f1e13dee95cb50f71e0bd84caaa5ee7210c1bb771da400df5045c2,
```

and the fixed H19 carrier hash is

```text
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b.
```

### Proposition 8.1 (positive soundness)

Every `FEASIBLE`/`OPTIMAL` word emitted by this script is an unconditional
literal length-6457 certificate.

#### Proof

`build_model` supplies the exact common negative-window prefix.  Calling
`ClearObjective()` clears both integer and floating objectives; the remaining
`explicit>=minimum` row is an ordinary feasibility constraint.  Every target
outside the pool is forced to one selected prefix cell.  Suffix letters are
nonzero, and the recurrence

```text
U[left,right] = U[left,right-1] OR suffix[right]
```

is enforced bitwise by Boolean `MaxEquality`.  A suffix witness implies all
15 bits of one interval OR equal its target, while the pool coverage row
forces either a prefix witness or at least one such suffix witness.  The
reverse implication “interval OR equals target implies witness” is not
encoded and is unnecessary: existential coverage needs one chosen exact
witness, and any literal solution can set one corresponding flag.  The
per-interval `AtMostOne` is redundant—one interval cannot have two distinct
OR labels—but sound.  Finally, the decoded concatenation is rejected unless
direct enumeration covers all 32,767 nonzero masks.  \(\square\)

At `s=19` the already-running suffix-only regression adds exactly

```text
285 suffix-letter bits;
2,565 proper interval-OR bits;
6,460 witness bits = 34 * C(20,2).
```

The source forces `16,349=16,383-34` nonpool targets into the prefix.  Its
default `minimum_explicit=16,362` forces at least 13 pool targets into the
prefix as well, so at most 21 pool targets may rely only on suffix witnesses.

### Proposition 8.2 (exact negative scope)

An `INFEASIBLE` result excludes exactly the following prescribed
decomposition, not all length-6457 words:

1. the fixed resident H19 path and its upper-perfect prefix;
2. every lower target outside the 34-mask heuristic pool has an explicit
   short-prefix witness;
3. each pool target has a short-prefix or suffix-only witness;
4. at least 16,362 targets have selected prefix witnesses; and
5. no target relies only on a prefix/suffix crossing interval.

The 34 masks are the union of four earlier 21-hole residual sets; that
provenance does not make the pool exhaustive.  The exact interval theorem has
247 suffix-ending intervals at `s=19`, whereas this regression instantiates
only the 190 suffix-only intervals.  It omits precisely

\[
 3\cdot19=57                                             \tag{8.1}
\]

crossing intervals, starting at one of the last three prefix positions.
Within the 34-mask pool these are 1,938 raw additional witness options.

This omission is only a restriction.  A selected crossing witness labelled
`X` would have to delete every outside-`X` incidence jointly on its last-one-
to-three prefix letters and its suffix portion, while retaining every bit of
`X` somewhere across the whole interval.  The current independent prefix and
suffix models contain no such selector or common blocker coupling, so they
cannot falsely certify it.  They can only miss a valid crossing-dependent
solution.  Likewise, `minimum_explicit=16,362` is heuristic: no length bound
forces that threshold because one suffix can realize many comparable masks.

Accordingly the executed suffix-only script is adopted as the first
**positive-sound Benders regression and restricted negative screen**.  It
should not be duplicated or cited as the full Section 4 oracle.

### The current crossing version is still a restriction

Current SHA `163f09fe...` enumerates the correct 57 crossing shapes, computes
their literal interval ORs exactly, and has `247` tail candidates and
`34*247=8,398` pool witness literals.  This makes every positive output sound,
but it does not yet implement the joint maximal closure.  The imported prefix
model has already imposed

\[
 z_{p,x}+\sum_{f\in\mathcal B^{\rm prefix}_{p,x}}y_f\ge1. \tag{8.2}
\]

If a crossing witness labelled `X` omits `x` at a supported prefix-tail
position, its exact-OR implication forces `z_(p,x)=0`, but that witness is not
present in the blocker sum in (8.2).  It is therefore usable only when some
independently selected prefix interval already justifies the same deletion.
In the exact closure, the crossing witness itself is a valid blocker.  Hence
the current crossing model can reject a word whose crossing interval is the
sole deletion reason.  This again narrows UNSAT and cannot create a false
positive.

The exact successor must rebuild (8.2) with both prefix and selected crossing
blockers before imposing the equivalence, or abandon maximal-prefix `z` and
use the discretionary direct-letter/occurrence CEGAR (5.7a)--(5.7c).  Merely
adding the 57 OR recurrences after `build_model` cannot repair the old lower
bound.  The pool and `minimum_explicit` restrictions remain even after this
coupling is fixed.

Source arithmetic gives the current crossing model exactly `178,203`
variables and `1,180,817` constraints on H19/pool34/s19.  The solver-free
companion

```text
scratch/audit_ad_k15_suffix_benders_regression_20260729.py
```

freezes all current hashes, independently checks the rank-eight deck,
residence, unrestricted linear upper coverage, `19,311/133,852/32,202`
prefix counts, the `190+57=247` interval split, and the current auxiliary
arithmetic.  It returns `PASS` without importing OR-Tools.

The H100 log has already frozen the built dimensions

```text
16,383 targets, 19,311 prefix cells, 133,852 prefix edges,
32,202 prefix incidences, 34 pool masks, 190 suffix intervals,
6,460 suffix witnesses.
```

At the time of this audit the run was still active; no feasibility or
infeasibility conclusion is inferred from elapsed time.

## 9. Reproducibility and code findings

At the final inspection, the underlying prefix optimizer
`optimize_k15_exact_compiler_maxcoverage.py` had

```text
sha256 ddfaae62316f27dd4221883dabf85b94910021b5b6291527a3b1ab012e83edda
```

and `330` lines.  It changed during the audit from an earlier 301-line copy;
the concurrent change added `--require-mask` and `--minimum-explicit`
controls.  The semantic core audited in Sections 2--5 remained the same.

Code-level conclusions:

1. the blocker equivalence, positive witness, middle witness, and nonempty
   constraints are exact;
2. the imported individual-edge filter is exactly (2.4)--(2.6);
3. the objective is exact maximum prefix coverage by Theorem 2.1;
4. the callback's literal append is a valid verified upper bound, but not an
   exact total-length objective;
5. its `load_middle` validator must not be reused unchanged in the future
   joint master: it omits an explicit rank-eight histogram assertion and
   tests fixed-length upper windows rather than the corrected unrestricted
   accumulated-union semantics; the frozen H19 input independently passes
   those stronger checks, so this does not affect Proposition 8.1; and
6. this audit launched no heavy local or remote computation.  It only read
   the status of the user's already-running H100 CPU regressions.
