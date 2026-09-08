# Exact arbitrary-width upper-interval oracle in binary `c`-space

Date: 2026-07-29

Status: complete theorem, exact integral separator, exact Boolean/CNF block,
and a shared next-occurrence CP-SAT formulation.  No solve is reported.

## 1. Verdict on the current implementation

The audited source was

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/cword.py
SHA-256 e9a01efc1edf5df791b1238854c66a678f7228b2b8fdf7ee19540bddbebf6abd
```

at the time of this audit.  Its physical `audit()` is logically complete for
upper coverage: it keeps extending a cyclic interval until its union is
`FULL`.  Its persistent upper CEGAR row is not complete.  For a target of
rank `R+q`, the caller supplies widths `q,q+1,q+2`, and the rank test inside
`cover_upper()` rejects width `q`; only widths `q+1,q+2` remain.  These are
sufficient witness widths, not necessary witness widths.  Consequently a
reported `PASS` remains sound because it is independently audited, whereas
an `UNSAT` obtained while retaining these rows is only an `UNSAT` statement
for the short-witness subclass.

Here is a local Johnson counterexample to the width implication.  Let
`k=9`, `R=5`,

\[
 S=\{a,b,c,d,e,f,g,h\},
\]

and take the bounded `S`-contained run

\[
 abcgh,\ bcdgh,\ bcegh,\ cdegh,\ bdegh,\ befgh.       \tag{1.1}
\]

Precede it by `zbcgh` and follow it by `zefgh`.  Every adjacent pair is a
rank-five Johnson pair.  The six contained columns union to `S`; the first
five omit `f`, the last five omit `a`, and hence no subwindow of width at
most five covers `S`.  Here `q=3`, while the current persistent row permits
only widths four and five.  This is a local implication counterexample, not
a claim that (1.1) already extends to a strict carrier.

All old short-width upper rows must therefore be removed before an
unrestricted-upper `UNSAT` claim.  Merely adding exact rows alongside them
does not remove their false restriction.

## 2. Binary strict-spiral setting

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r}=kN,
\]

and let `c` be the cyclic binary word of length `W`.  Put

\[
 p(i,x)=i-xN\pmod W,
 \qquad
 a_{i,x}=c_{p(i,x)},
 \qquad
 T_i=\{x:a_{i,x}=1\}.                                \tag{2.1}
\]

The class-sum equations give `|T_i|=r`.  They also give

\[
 \sum_{i=0}^{W-1}a_{i,x}=\sum_{p=0}^{W-1}c_p=rN>0   \tag{2.2}
\]

for every coordinate `x`, so every coordinate occurs.  Moreover

\[
 T_{i+N}=\rho T_i.                                    \tag{2.3}
\]

Fix an upper target `S`, with

\[
 r<|S|=r+q\le k.
\]

For a proper target `S` define

\[
 b_i={\bf1}_{\{T_i\subseteq S\}},
 \qquad O_i=S\setminus T_i\quad(b_i=1).              \tag{2.4}
\]

Every `O_i` has size `q`.

## 3. Contained-run and sharp Helly theorem

### Theorem 3.1 (maximal contained runs)

Let \(\mathcal G_S=\{i:b_i=1\}\), and let its components be maximal cyclic
runs.
Then the following are equivalent:

1. some cyclic interval of the middle chronology has union `S`;
2. some interval contained in \(\mathcal G_S\) has empty omitted intersection;
3. some maximal run `R` of \(\mathcal G_S\) satisfies

   \[
   \bigcap_{i\in R}O_i=\varnothing;
   \]

4. some maximal run `R` satisfies

   \[
   \bigcup_{i\in R}T_i=S.                            \tag{3.1}
   \]

#### Proof

An interval whose union is `S` contains only sets contained in `S`, hence it
lies in one maximal good run.  For every contained interval `I`,

\[
 S\setminus\bigcup_{i\in I}T_i
   =\bigcap_{i\in I}(S\setminus T_i).                \tag{3.2}
\]

Enlarging `I` inside its maximal run can only shrink this intersection.
Thus a witnessing interval makes its maximal run a witness, and a maximal
run with empty intersection is itself a witnessing interval.  This proves
all equivalences.  ∎

### Lemma 3.2 (sharp finite Helly number)

If a family of `q`-subsets has empty intersection, at most `q+1` members
already have empty intersection.

#### Proof

Choose one member `O_0`.  For every `x in O_0`, choose a family member which
omits `x`; together with `O_0` these at most `q+1` sets have empty
intersection.  The bound is sharp: the `q+1` complements of singletons on a
`(q+1)`-set form a minimal empty-intersection family.  Their complements
inside `S` are even a Johnson clique.  ∎

The lemma bounds the number of landmark columns, not the chronological span
between them.  Repeated or recycled insertions may separate the landmarks
by an arbitrarily long contained run.  It therefore supplies no `q+2`
window bound.

## 4. Exact next-occurrence flag theorem

For a fixed integral `c`, define its cyclic next-one distance

\[
 d(p)=\min\{e\in\{0,\ldots,W-1\}:c_{p+e}=1\},
 \qquad
 \delta_i(x)=d(p(i,x)).                               \tag{4.1}
\]

The minimum exists by (2.2).

### Theorem 4.1 (ordered next-occurrence criterion)

For every start `i` and endpoint offset `ell`,

\[
 \bigcup_{e=0}^{\ell}T_{i+e}
   =\{x:\delta_i(x)\le\ell\}.                       \tag{4.2}
\]

For every proper upper target `S`, an interval beginning at `i` has union
`S` if and only if

\[
 \boxed{
 \max_{x\in S}\delta_i(x)
   <\min_{y\notin S}\delta_i(y).}                   \tag{4.3}
\]

When (4.3) holds, the shortest witnessing offset is the left-hand maximum.

#### Proof

A coordinate `x` belongs to the union through offset `ell` exactly when its
first occurrence at or after `i` has distance at most `ell`, proving (4.2).
The union is exactly `S` precisely when every coordinate of `S` has appeared
and no coordinate outside `S` has appeared.  Such an integer `ell` exists
exactly when the maximum required arrival precedes the minimum forbidden
arrival, and the maximum is then the first valid endpoint.  ∎

Assume now the eager Johnson equations.  The positive values
`delta_i(x)`, for `x notin T_i`, are pairwise distinct: a tie would make two
previously unseen coordinates enter in the same Johnson transition.  Thus
the absent coordinates have a definite first-arrival order

\[
 x_{i,1},\ldots,x_{i,k-r},
\]

and all distinct arbitrary-width unions beginning at `i` are exactly the
saturated flag

\[
 T_i\subset T_i\cup\{x_{i,1}\}\subset\cdots
 \subset T_i\cup\{x_{i,1},\ldots,x_{i,k-r}\}=[k].    \tag{4.4}
\]

Waiting and recycled insertions change physical widths, but not this flag.
Equation (2.3) gives

\[
 \delta_{i+N}(x)=\delta_i(x-1),                      \tag{4.5}
\]

so the flag at `i+N` is the rotation of the flag at `i`.  Consequently an
all-orbit audit needs only `N` starts, with exactly one quotient slot at each
upper depth and `N(k-r)` slots in total.  At `k=15`, this is

\[
 429\cdot7=3003.                                     \tag{4.6}
\]

Burnside's lemma gives the rank-`s` target-orbit count

\[
 M_s=\frac1k\sum_{d\mid\gcd(k,s)}
       \varphi(d)\binom{k/d}{s/d};                   \tag{4.7}
\]

a rotation with cycle length `d` fixes precisely the masks constant on its
cycles, and those fixed masks choose `s/d` of the `k/d` cycles.  At `k=15`,
the numbers for ranks `9,...,15` are

\[
 335,201,91,31,7,1,1.                                \tag{4.8}
\]

They may be compared against the canonicalized flags in (4.4).  Computing
all `d(p)` takes one cyclic backward scan.  Sorting the `k` distances at each
of the `N` base starts and canonically rotating each of the `N(k-r)` produced
flag masks gives a complete straightforward audit in

\[
 O\bigl(W+Nk\log k+Nk(k-r)\bigr)=O(Wk).              \tag{4.9}
\]

Generating and canonicalizing every target mask costs an additional
`O(k 2^k)=O(k^2W)` once.  Since `2^k <= (k+1)W`, this is polynomial in the
explicit `c`-space size.  Pretabulated orbit representatives remove that
repeated preprocessing term.

## 5. Audit of the proposed cyclic omitted-core recurrence

For `x in S`, define cyclic Boolean states by

\[
 \boxed{
 q_{i,x}
 =\neg b_i\ \vee\
   \bigl(q_{i-1,x}\wedge\neg a_{i,x}\bigr).}         \tag{5.1}
\]

The proposed recurrence is exact, with `q=1` meaning that the coordinate is
still unseen in the current maximal `S`-contained run.

### Theorem 5.1 (state invariant and cyclic uniqueness)

If `[j,i]` is the prefix through `i` of a maximal good run, then

\[
 q_{i,x}=1
 \quad\Longleftrightarrow\quad
 x\notin\bigcup_{t=j}^{i}T_t.                        \tag{5.2}
\]

For every proper `S`, the cyclic system (5.1) has a unique solution, and

\[
 \boxed{
 S\text{ is covered}
 \Longleftrightarrow
 \bigvee_{i=0}^{W-1}
 \left(b_i\wedge\bigwedge_{x\in S}\neg q_{i,x}\right).} \tag{5.3}
\]

#### Proof

At a bad position, (5.1) sets every `q_{i,x}` to one.  The first good
position therefore initializes the state to `S minus T_i`; every later good
position intersects the current unseen set with `S minus T_i`.  This proves
(5.2) by induction.

Because `S` is proper, choose `y notin S`.  Equation (2.2) gives a position
containing `y`, hence a bad position.  Its forced all-one state anchors the
cyclic recurrence and deterministic propagation gives uniqueness.  Finally,
all states are zero at a good endpoint exactly when the prefix of its maximal
good run has union `S`.  Apply Theorem 3.1.  ∎

Hamiltonicity is therefore sufficient for the reset claimed in the prompt,
but is stronger than necessary: the `c`-space class sums already force it.
For `S=[k]`, full coverage is automatic from (2.2).  The recurrence also has
the unique all-zero state, but the proper-target reset proof should not be
quoted for that case.

## 6. Exact CNF and CP-SAT block

The containment variable is defined exactly by

\[
 b_i\longleftrightarrow\bigwedge_{y\notin S}\neg a_{i,y}. \tag{6.1}
\]

Its CNF is

\[
 \neg b_i\vee\neg a_{i,y}\quad(y\notin S),
 \qquad
 b_i\vee\bigvee_{y\notin S}a_{i,y}.                 \tag{6.2}
\]

For `p=q_{i-1,x}`, `z=a_{i,x}`, and `q=q_{i,x}`, equation (5.1) is exactly
the following four clauses:

\[
\begin{array}{ll}
 b_i\vee q,&
 \neg p\vee z\vee q,\\
 \neg q\vee\neg b_i\vee p,&
 \neg q\vee\neg b_i\vee\neg z.
\end{array}                                           \tag{6.3}
\]

All four directions are required.  Introduce endpoint selectors `e_i` and
add

\[
 \neg e_i\vee\neg q_{i,x}\quad(x\in S),
 \qquad \bigvee_i e_i.                               \tag{6.4}
\]

The implication `e_i -> b_i` is redundant because a bad position forces
all its `q` states to one, but it may be retained for readability.  No
reverse implication defining `e_i` is needed: the existential final clause
makes (6.4) satisfiable exactly when an accepting endpoint exists.

For `s=|S|`, the block uses `W(s+2)` auxiliary Booleans and, omitting the
redundant selector-to-`b` clauses,

\[
 W(k+4s+1)+1                                         \tag{6.5}
\]

clauses.  In CP-SAT notation, (6.2)--(6.4) are direct `AddBoolOr` rows; every
membership literal is the existing variable

```text
c[(i - x*N) % W].
```

One fixed representative `S` is enough.  If `rho^t S` is covered, shifting
the witnessing interval by `-tN` covers `S`; conversely a witness for `S`
rotates to witnesses for its whole orbit.  This remains true for short
orbits at composite `k`.

## 7. A zero-auxiliary exact integral separator

The recurrence is a one-shot target block.  For ordinary CEGAR, there is a
smaller exact cut.

Let `c*` be an integral incumbent missing proper target `S`.  At every bad
position `i`, choose

\[
 y_i\in T_i\setminus S,
\]

so `c*_(p(i,y_i))=1`.  For every maximal good run `R`, choose

\[
 x_R\in S\setminus\bigcup_{i\in R}T_i,
\]

which exists by Theorem 3.1, so `c*_(p(i,x_R))=0` throughout `R`.

### Theorem 7.1 (run-blocker clause)

Every `c` which covers `S` satisfies

\[
 \boxed{
 \sum_{i:\,b_i=0}\bigl(1-c_{p(i,y_i)}\bigr)
 +\sum_R\sum_{i\in R}c_{p(i,x_R)}\ge1.}             \tag{7.1}
\]

The incumbent `c*` violates (7.1).

#### Proof

Suppose every literal on the left retains its incumbent value.  Each old bad
position still contains its chosen outside coordinate, so it remains bad.
Every new `S`-contained run is therefore contained in one old run `R`.  The
chosen blocker `x_R` remains absent at every position of `R`, so no such run
can union to `S`.  The contrapositive proves validity.  Every displayed term
is zero at `c*`.  ∎

Before alias deduplication, (7.1) has exactly one literal per physical
position, hence `W` literals.  Opposite-polarity aliases cannot occur: they
would require the same incumbent bit to equal both zero and one.  The cut
therefore drops directly into the existing partial-no-good representation

```text
("nogood", [(c_index, incumbent_value), ...]).
```

Although its comment mentions an exact column pattern, the current builder
already accepts an arbitrary partial assignment and emits precisely the
clause (7.1).

This is a complete polynomial-time separation oracle for integral binary
`c` candidates.  Given a missing target `S` (or a pretabulated target-orbit
list), it audits `S` and emits a globally valid cut in `O(kW)` time and zero
auxiliaries.  Straightforward one-time generation/canonicalization of all
target representatives costs `O(k2^k)=O(k^2W)`.  Repeated separation is
finite because each cut excludes the incumbent, but no polynomial bound on
the number of CEGAR rounds is claimed.

## 8. Shared next-distance CP-SAT compression

The next distances can instead be variables paid once for every upper
target.  Introduce integers `D_p in [0,W-1]` and impose, cyclically,

\[
 c_p=1\Longrightarrow D_p=0,
 \qquad
 c_p=0\Longrightarrow D_p=D_{p+1}+1.                \tag{8.1}
\]

Since the class sums force at least one `1`, (8.1) has the unique solution
`D_p=d(p)`.  The `+1` is an ordinary integer equality, not a congruence.

For one proper target `S`, introduce one start variable `a in [0,W-1]` and,
for each coordinate `x`, the element view

\[
 E_x=\operatorname{Element}
 \left(a,\bigl(D_{j-xN}\bigr)_{j=0}^{W-1}\right).   \tag{8.2}
\]

Set

\[
 A=\max_{x\in S}E_x,
 \qquad B=\min_{y\notin S}E_y,
\]

and impose

\[
 A+1\le B.                                           \tag{8.3}
\]

By Theorem 4.1, (8.1)--(8.3) are an exact one-shot arbitrary-width CP-SAT
formulation.  The global `W` distance variables are shared; each target adds
one start, `k` element views, two extrema, and `O(kW)` element incidence.
The Boolean recurrence of Section 6 is preferable when predictable pure-CNF
size and propagation are more important than auxiliary-variable count.

No LP/TU claim is made for relaxed start, selector, or recurrence variables.
The theorem is integral and exact.

## 9. Integration and scope

An exact replacement of the current upper CEGAR loop may use either:

1. the complete next-occurrence audit plus one run-blocker clause (7.1) for
   each selected missing orbit representative;
2. one recurrence block (6.1)--(6.4) per repeatedly missing target; or
3. the shared-distance block (8.1)--(8.3).

The zero-auxiliary replacement needs no new builder branch.  For each
audited missing representative `orb`, the integration is literally

```text
clause = upper_blocker_clause(c, K, E.N, orb)
assert clause is not None and clause
lazy.append(("nogood", clause))
```

starting from a fresh `lazy` list.  By contrast, promoting a target to the
recurrence block requires a new `upper_exact` lazy kind which recreates its
auxiliaries on every model rebuild.  The recurrence helper assumes the
class-sum equations already present in `build_cpsat()`; it is not a
standalone exact constraint on an otherwise arbitrary `c` array.  The
run-blocker clause itself needs no such precondition.

A practical hybrid uses the zero-auxiliary clauses first and promotes a
repeated target to a one-shot exact block.  Wrapping good runs must be treated
as single cyclic components.  An all-bad target gives only the bad-position
literals.  The full target is automatic.  A full-cycle interval may use all
`W` distinct positions but must not reuse a position.

The following logical scopes remain mandatory:

* `MAXROUNDS` is not a conclusion;
* an `UNSAT` under `--radius` remains radius-scoped;
* every old short-width upper row must be absent;
* all other retained lazy rows need their own validity proofs; and
* exact upper coverage closes only the carrier's upper-shadow gate.  It does
  not provide residence, lower shadows, a one-core, Hall matching, safe cut,
  or literal compiler.

## 10. Reference implementation and lightweight audit

The solver-free reference implementation is

```text
scratch/cword_exact_upper_oracle_20260729.py
SHA-256 8f8ae59a6900a68563e6f5df13ff14a9adb4ec35224889875337b80617982417
```

It implements the exact next-occurrence atlas, fixed-target witness test,
run-blocker clause, and the CNF/CP-SAT recurrence builder.  Its tiny
`k=5` self-test exhausts all 100 class-sum words, compares the
next-occurrence atlas with literal cyclic interval enumeration, and checks
all 75 resulting blocker clauses against every covering class-sum word.  The
reproduced output is

```text
OK k=5 class_sum_words=100 globally_checked_blocker_clauses=75
```

This solver-free regression exercises the atlas and blocker clauses.  It
does not instantiate OR-Tools, so a production `upper_exact` builder branch
still requires a separate solver smoke test in the environment that owns
`cword.py`.
