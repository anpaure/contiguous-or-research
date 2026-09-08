# The `K17` two-bank `D2` schedule has an exact rank-three common-cap interface

Date: 2026-07-31  
Status: exact compiler theorem conditional on a literal two-bank
`D2` row; the repaired six-swap port flow and upper-complete chronology remain
open

## 0. Result

Put

\[
 W={17\choose8}=24310,\qquad L=W+3=24313.
\]

Suppose a proposed two-bank construction has produced a literal length
`W+1` depth-two row

\[
                    Z=(Z_0,\ldots,Z_W)                 \tag{0.1}
\]

with `a` distinct rank-nine owner tokens and `W+1-a` distinct rank-eight
facet tokens.  Assume that the row has the intended owner/palette coverage,
that adjacent tokens have union rank at least nine, and that all upper
targets are already witnessed by intervals of length at least three.

Then the remaining lower compiler has a completely finite exact interface.

1. `Z` is the second derivative of a nonempty word if and only if its maximal
   three-window envelope is nonempty and replays every row.  Equivalently,
   apart from nonemptiness, every strictly internal coordinate run in `Z`
   must have length at least three.
2. Every lower target not already occurring as a rank-eight token of `Z`
   must use a singleton or adjacent-pair cell.  Their exact number is

   \[
        41224+a,                                      \tag{0.2}
   \]

   while the number of such cells is `48625`.  Thus

   \[
        \boxed{a\le7401}                              \tag{0.3}
   \]

   is a necessary scalar guard, with residual slack `7401-a`.
3. After fixed short prepins are incorporated, an injective target--cell
   assignment is realizable by one common cap if and only if it avoids an
   explicit obstruction clutter of rank at most three.  Rank three is sharp.
4. A stronger permanent-bit/host condition turns the problem into ordinary
   bipartite Hall.  This is a constructive sufficient condition for the
   connector and compiler lanes.

For the new six-occurrence-swap repaired macro forest, the marked closure has
`3815` owner tokens in `106` internally clean components.  If a repaired
port solution joins them by exactly `105` one-token pure owners, then

\[
 a=3815+105=3920.                                    \tag{0.4}
\]

The conditional compiler ledger is therefore

```text
marked rank-nine D2 tokens                 3920
complementary rank-eight D2 tokens        20391
residual rank-eight targets                3919
all residual lower targets                45144
singleton/adjacent-pair cells              48625
scalar residual slack                       3481
```

This is a genuine positive capacity result, not a completed `K17` word.  The
marked path, complementary facet path, upper coverage, and common-cap
matching have not yet been constructed simultaneously.

In fact the fixed-endpoint connector face is already known to be
infeasible: its clean component graph has five weak components, including
one isolated component, so at least four noncatalogue socket actuators are
necessary.  Thus (0.4) is the **token-neutral baseline**.  If those actuators
change the number of owner tokens by a net amount `delta` while preserving
the fixed `W+1` depth-two length, then

\[
                 a=3920+\delta,
 \qquad \text{scalar slack}=3481-\delta.             \tag{0.5}
\]

If an actuator changes the rank profile more generally, the distinct-facet
formula in Section 3, rather than (0.5), is authoritative.

## 1. Linear derivative and the exact inversion test

For a nonempty word `A=(A_0,...,A_(L-1))`, write

\[
 (DA)_i=A_i\cup A_{i+1}.
\]

Thus

\[
 (D^2A)_i=A_i\cup A_{i+1}\cup A_{i+2},\qquad 0\le i\le L-3.
                                                               \tag{1.1}
\]

For an arbitrary proposed row `Z` of length `L-2`, define its maximal
three-window envelope

\[
 E_p=\bigcap_{\substack{0\le i\le L-3\\i\le p\le i+2}}Z_i,
 \qquad 0\le p<L.                                  \tag{1.2}
\]

The intersection is truncated at the two linear boundaries.  There is no
cyclic wrap after opening.

### Theorem 1.1 (exact `D2` inversion)

There is a nonempty word `A` with `D^2A=Z` if and only if

\[
 E_p\ne\varnothing\quad(0\le p<L)                  \tag{1.3}
\]

and

\[
 E_i\cup E_{i+1}\cup E_{i+2}=Z_i
 \quad(0\le i\le L-3).                             \tag{1.4}
\]

When these conditions hold, `A=E` is the coordinatewise maximal realizing
word.

#### Proof

Every realizing letter `A_p` is contained in each row `Z_i` whose
three-window contains `p`, and hence \(A_p\subseteq E_p\).  Therefore
nonemptiness and (1.4) are necessary.  Conversely (1.3)--(1.4) say exactly
that the nonempty word `E` has second derivative `Z`.  Maximality follows
from the first containment.  \(\square\)

For an interior row, (1.4) is the five-token identity

\[
\begin{split}
 Z_i={}&(Z_{i-2}\cap Z_{i-1}\cap Z_i)\\
      &\cup(Z_{i-1}\cap Z_i\cap Z_{i+1})\\
      &\cup(Z_i\cap Z_{i+1}\cap Z_{i+2}),           \tag{1.5}
\end{split}
\]

with the evident truncation near an endpoint.

### Corollary 1.2 (run form)

Equation (1.4) holds if and only if every strictly internal positive run of
every coordinate trace of `Z` has length at least three.  Runs meeting a
linear endpoint may have any positive length.

Indeed, a coordinate belongs to `E_p` precisely when all `Z` rows whose
windows contain `p` contain it.  In the interior this is the length-three
erosion of its binary trace.  Dilating that erosion by the same
three-window recovers exactly the boundary runs and the internal runs of
length at least three.

In particular, once (1.4) holds, every strict internal positive run in
`DZ` has length at least four.  This is exactly the `D2/D3` residence
dilation used by the nonflat owner/cofacet zipper.  Envelope nonemptiness
(1.3) remains an independent requirement.

## 2. Longer intervals are fixed by `Z`

### Lemma 2.1 (deep-interval invariance)

If a word `Q` satisfies `D^2Q=Z`, then every interval `[r,s]` of length at
least three satisfies

\[
 \bigcup_{p=r}^{s}Q_p
   =\bigcup_{i=r}^{s-2}Z_i.                          \tag{2.1}
\]

#### Proof

The right side is the union of the three-windows
`Q_i union Q_(i+1) union Q_(i+2)` for `r<=i<=s-2`.  Those windows cover
exactly the positions `r,...,s`.  \(\square\)

Consequently, once `Z` is fixed and replays exactly, no later lower cap can
destroy an upper or deep-shadow witness whose physical cell has length at
least three.  Upper/deep completeness is therefore a property of the
two-bank chronology `Z`, not of the residual lower matching.  An independent
singleton or pair witness is different and must be treated as a fixed
prepin below.

## 3. Exact lower ledger and the `7401-a` guard

Let

\[
 \mathcal L^-=\bigsqcup_{r=1}^{8}{[17]\choose r},
 \qquad |\mathcal L^-|=65535.                       \tag{3.1}
\]

The intended repaired-forest output has a sharper Johnson form.  Let

\[
 P=(P_1,\ldots,P_a),\qquad Q=(Q_1,\ldots,Q_b),
 \qquad a+b=W,                                      \tag{3.2}
\]

partition all rank-nine owners.  Assume that

\[
 P_1,\ldots,P_a,Q_1,\ldots,Q_b,P_1                 \tag{3.3}
\]

is a lower-rainbow Johnson cycle.  Define

\[
\begin{aligned}
 C_i&=P_i\cap P_{i+1} &&(1\le i<a),\\
 F_0&=P_a\cap Q_1,\\
 F_j&=Q_j\cap Q_{j+1} &&(1\le j<b),\\
 F_b&=Q_b\cap P_1.
\end{aligned}                                                    \tag{3.4}
\]

### Lemma 3.1 (two-bank Johnson zipper)

The depth-two row

\[
 Z=(P_1,\ldots,P_a,F_0,\ldots,F_b)                 \tag{3.5}
\]

has length `W+1`, and

\[
 DZ=(P_1\cup P_2,\ldots,P_{a-1}\cup P_a,
       P_a,Q_1,\ldots,Q_b).                         \tag{3.6}
\]

The direct facet bank is exactly `{F_0,...,F_b}`, while the residual
rank-eight targets are exactly `{C_1,...,C_(a-1)}`.

#### Proof

Two distinct rank-eight facets of the same rank-nine owner have union equal
to that owner.  Hence `P_a union F_0=P_a` and
`F_(j-1) union F_j=Q_j` for every `j`.  This proves (3.6).  The lower-rainbow
hypothesis says that the `a-1` colours `C_i` and the `b+1` colours `F_j` are
pairwise distinct and together enumerate all `W` rank-eight targets.
\(\square\)

Thus the exact port-flow output needed by the primary route is not merely a
marked path and a complement path.  Their two cross incidences must make
(3.3) lower-rainbow.  The common-cap compiler then receives the `F` bank as
direct rows and the `C` bank as its residual rank-eight part.

For residence, the marked word `P` and facet word `F` must jointly have no
strict internal run below three.  A useful sufficient condition on the
complement is minimum strict owner-run four on `Q`, because adjacent
intersection shortens each proper run by one.  The two cross interfaces
still require the global run/envelope replay of Section 1.

Assume the `W+1-a` rank-eight entries of `Z` are pairwise distinct and every
other entry has rank nine.  They directly cover `W+1-a` lower targets.
The residual family is

\[
 \mathcal R_Z=\mathcal L^-
    \setminus\{Z_i:|Z_i|=8\}.                       \tag{3.7}
\]

Since

\[
 \sum_{r=1}^{7}{17\choose r}=41225,
\]

we have

\[
 |\mathcal R_Z|=41225+(a-1)=41224+a.                \tag{3.8}
\]

### Lemma 3.2 (all residual cells are short)

If every adjacent pair `Z_i,Z_(i+1)` has union rank at least nine, then no
target in `R_Z` can be realized by an interval of length at least three.

#### Proof

An interval of length three has OR equal to one `Z_i`.  Its lower-rank value
is therefore one of the already removed direct rank-eight targets.  An
interval of length at least four contains two adjacent three-windows and
its OR contains `Z_i union Z_(i+1)`, of rank at least nine.  \(\square\)

There are exactly

\[
 L+(L-1)=24313+24312=48625                          \tag{3.9}
\]

singletons and adjacent pairs.  Injectivity of target witnesses therefore
gives (0.3), and the exact scalar slack is

\[
 48625-(41224+a)=7401-a.                            \tag{3.10}
\]

More generally, if `d_8` is only the number of **distinct** direct
rank-eight rows, the residual count is `65535-d_8` and the scalar slack is
`d_8-16910`.  Thus duplicate facet rows consume the scalar reserve one for
one.

A fixed short prepin which itself witnesses one residual lower target
removes one target and one cell, leaving (3.10) unchanged.  An auxiliary
short cap which consumes a cell without discharging a lower target reduces
the slack by one.

## 4. The maximal common cap

Let `P_0` be a set of already fixed singleton/pair occurrences `(R,K)` with
pairwise distinct targets and cells.  Remove their targets and cells from
the residual instance, and put

\[
 B_p=E_p\cap
     \bigcap_{\substack{(R,K)\in P_0\\p\in K}}R.     \tag{4.1}
\]

Before any residual matching, fail closed unless

\[
\begin{aligned}
 B_p&\ne\varnothing &&(p),\\
 B_i\cup B_{i+1}\cup B_{i+2}&=Z_i &&(i),             \tag{4.2}\\
 \bigcup_{p\in K}B_p&=R &&((R,K)\in P_0).
\end{aligned}
\]

For an unpinned residual target `S` and an unused singleton or pair `J`, the
incidence `(S,J)` is individually feasible exactly when

\[
 B_p\cap S\ne\varnothing\quad(p\in J),
 \qquad
 S\subseteq\bigcup_{p\in J}B_p.                     \tag{4.3}
\]

Choose one incidence for every residual target and use every cell at most
once.  For a selection `M`, define

\[
 Q_p(M)=B_p\cap
        \bigcap_{\substack{(S,J)\in M\\p\in J}}S.    \tag{4.4}
\]

### Theorem 4.1 (exact common-cap criterion)

The selection `M` is realized by one nonempty physical word if and only if

\[
\begin{array}{ll}
\text{(P)}&Q_p(M)\ne\varnothing\quad\text{for every }p;\\[1mm]
\text{(D2)}&\displaystyle\bigcup_{p=i}^{i+2}Q_p(M)=Z_i
                       \quad\text{for every }i;\\[2mm]
\text{(F)}&\displaystyle\bigcup_{p\in K}Q_p(M)=R
                       \quad\text{for every }(R,K)\in P_0;\\[2mm]
\text{(L)}&\displaystyle\bigcup_{p\in J}Q_p(M)=S
                       \quad\text{for every }(S,J)\in M.
\end{array}                                                    \tag{4.5}
\]

When these conditions hold, `Q(M)` itself is the coordinatewise maximal
realizing word.

#### Proof

Every realizing word is contained positionwise in `B` and in every selected
target cap, hence in `Q(M)`.  Enlarging it to `Q(M)` cannot delete any
required bit.  Conversely, the intersections in (4.4) forbid all bits
outside every active fixed or selected label, while (4.5) supplies all
required bits and nonemptiness.  Thus `Q(M)` realizes every declared row.
Lemma 2.1 then preserves every longer interval.  \(\square\)

## 5. The exact obstruction clutter has rank three

Make one candidate vertex for every feasible incidence `(S,J)`, partitioned
by its target `S`.  Discard a set if it already selects two incidences from
one target part.  The inclusion-minimal failures of (4.5) are exactly:

1. two candidates using the same cell;
2. candidates through one position whose labels have empty intersection
   with `B_p`;
3. candidates omitting a bit `b in Z_i` whose cells cover every host
   `p in [i,i+2]` with `b in B_p`;
4. the analogous blocker for one fixed prepin bit; and
5. one selected anchor `(S,J)`, a bit `b in S`, and candidates omitting `b`
   whose cells cover every host for `b` inside `J`.

### Theorem 5.1 (rank-three conflict-transversal equivalence)

A one-incidence-per-target selection is an exact common-cap compiler if and
only if it contains none of the five obstruction types above.  Every
minimal obstruction has size at most three.

#### Proof

The five types are precisely failures of cell injectivity and the four rows
of (4.5).  Every failure contains an inclusion-minimal one.  Conversely,
absence of all five types gives every row of (4.5).

Only three short cells meet an interior position: its singleton, left pair,
and right pair.  Hence a minimal empty-position blocker has size at most
three.  A `D2` row has three host positions, so its minimal bit cover has
size at most three.  A fixed singleton/pair has at most two hosts.  A
selected residual target contributes its anchor plus at most two other host
blockers.  Cell collisions have size two.  \(\square\)

Equivalently, with selector variables `y_e`, use the matching equations and
all bad-pair/bad-triple cuts

\[
 \sum_{e\in D_S}y_e=1,\qquad
 \sum_{e:\,J(e)=J}y_e\le1,\qquad
 \sum_{e\in F}y_e\le |F|-1.                         \tag{5.1}
\]

This integral system is necessary and sufficient.  Rank three is sharp:
at one position with envelope `{1,2,3}`, let its three incident cells carry
labels `{2,3}`, `{1,3}`, `{1,2}`.  Every pair leaves a nonempty cap, while
the triple deletes the position.

Bounded rank does not imply bounded dependency.  Many target candidates can
still meet the same physical position, so no generic symmetric LLL or
nibble theorem follows from Theorem 5.1 alone.

## 6. A guarded Hall sufficient theorem

Let `G` be a subgraph of the feasible residual target--cell graph.  Choose:

1. a permanent bit `a_p in B_p` at every position;
2. one host `h(i,b) in [i,i+2]` for every `b in Z_i`, with
   `b in B_(h(i,b))`;
3. one analogous host for every fixed-prepin bit; and
4. for every candidate `e=(S,J)` in `G` and every `b in S`, one host
   `g(e,b) in J` with `b in B_(g(e,b))`.

Assume:

* every candidate whose cell contains `p` has label containing `a_p`;
* every candidate whose cell covers a chosen `D2` or fixed-prepin host for
  `b` has label containing `b`; and
* whenever two candidates `e,f` are matching-compatible and the cell of
  `f` covers `g(e,b)`, the label of `f` contains `b`.

### Theorem 6.1 (guarded Hall lift)

Every target-saturating matching in `G` is an exact common-cap compiler.
Consequently it is sufficient that

\[
              |N_G(X)|\ge |X|                       \tag{6.1}
\]

for every set `X` of residual targets.

#### Proof

The permanent bits prove nonemptiness.  The fixed hosts preserve every bit
of every `D2` row and prepin.  If a selected anchor `e` requires bit `b`,
then `e` itself contains `b`, and every co-selected candidate whose cell
meets `g(e,b)` contains `b` by the last rule.  Hence `b` survives at that
host.  Theorem 4.1 applies, and Hall's theorem supplies the matching under
(6.1).  \(\square\)

This condition is sufficient, not necessary.  Its value is that a port or
Pascal construction can export literal guard bits and hosts, after which the
remaining compiler is only an ordinary bipartite matching.

## 7. The exact socket-to-compiler handoff

The repaired port lane should export the following tuple, not merely a
connected owner factor:

\[
   (Z,\;\mathcal P_0,\;B,\;G,\;a_p,\;h,\;g).          \tag{7.1}
\]

There are four fail-fast socket guards.

1. **Global inversion.**  Recompute (1.2) across every socket and bank
   interface.  At a cut between `Z_(c-1)` and `Z_c`, the two mixed envelope
   letters are

   \[
    E_c=Z_{c-2}\cap Z_{c-1}\cap Z_c,\qquad
    E_{c+1}=Z_{c-1}\cap Z_c\cap Z_{c+1}.              \tag{7.2}
   \]

   The four nearby row equations `c-2,...,c+1` must be replayed.  Envelopes
   computed separately on the two banks cannot be pasted.
2. **Direct-palette injectivity.**  The complementary facet tokens must be
   distinct.  Every duplicate spends one unit of (3.10).
3. **Short-cell accounting.**  A socket using a singleton/pair either
   discharges one distinct residual lower target or consumes one unit of
   scalar slack.  Its cap is included in (4.1).
4. **Guard neutrality.**  If port flow and lower matching are to be solved
   sequentially, every allowed socket/connector option must preserve the
   same `Z`, permanent bits, fixed hosts, and candidate-host rules.  If an
   option changes any of them, the connector column and common-cap choice
   must be selected jointly.

Every noncatalogue actuator must additionally export its net contribution to
`a` (or, more generally, its change in the number of distinct direct
rank-eight rows).  This is what updates the exact scalar ledger before the
candidate graph is built.

The last point is essential.  Marginal port `b`-flow plus marginal lower
Hall does not imply a common solution; the sharp rank-three obstruction can
involve three individually legal connector/cap choices.  On the owner side,
ordinary `b`-flow certifies only degrees.  The exact completion needs
occurrence-labelled pair columns, component-connectivity cuts, residence,
palette service, and the guard relation in (7.1).

For the fallback three-path atom witness, `a=5810` would give `18501`
direct facet rows, `47034` residual lower targets, and scalar slack `1591`.
Its two non-port joins are therefore not a scalar obstruction, but both must
pass the four guards above.  The repaired six-swap forest is the stronger
primary route because its conditional `a=3920` leaves `3481` units.

## 8. Exact proved/conditional boundary

Proved here:

* exact linear `D2` inversion and its run formulation;
* invariance of all intervals of length at least three after `D2` is fixed;
* the exact `7401-a` lower-cell ledger;
* the necessary-and-sufficient pair/triple common-cap system; and
* the guarded-Hall sufficient theorem and socket export state.

Exact authenticated input used for the primary calibration:

```text
scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 08ecea3f8730e6efb296e9d3d1df06c716935656681a988b71286b056ca00662
payload SHA-256 14a1c85f714462a37d8675daa0364de57f95a295fdcdaa135f1e7351aecf1995

scratch/k17_sixswap_macro_forest_20260731.flow.json
SHA-256 4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b
payload SHA-256 f1ab56555d744d2e527325c8617c2af1ee0f463ad13666f153d56efc588624db

MATH_AUDIT_K17_SIXSWAP_REPAIRED_COMPONENT_PATH_GATE_20260731.md
SHA-256 9c609c38f0ce1654dd4c0e3a127d9da7881f33c3ccca16af1d35811193b326d0
```

The first artifact records `106/154/3815` and zero strict internal `D2/D3`
debt after the six swaps; the second independently materializes the repaired
forest.  The compiler arithmetic uses only these counts and the zero-slack
identity that a path on `106` components uses `105` owners.

Still conditional:

* existence of the distinctly labelled residence-safe marked path with the
  at least four required noncatalogue socket actuators;
* connected complementary `U`-to-port completion;
* a distinct, exact complementary facet path;
* complete upper/deep coverage of the resulting `Z`; and
* Hall or pair/triple feasibility of its actual cap graph.

Thus this note is not a `K17` upper bound or an all-`k` theorem.  It gives the
exact compiler guard interface which any successful two-bank schedule must
now satisfy.
