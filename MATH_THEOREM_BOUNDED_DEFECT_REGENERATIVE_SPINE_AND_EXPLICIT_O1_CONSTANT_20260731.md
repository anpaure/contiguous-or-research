# Bounded-defect regenerative spines and an explicit additive constant

Date: 2026-07-31  
Status: exact implication and defect-propagation audit; no unconditional
all-`k` construction is claimed

## 0. Verdict

The exact RSB theorem asks for zero defect in every dimension.  For

\[
                         \nu(k)=B(k)+O(1)
\]

this is stronger than necessary in two different ways.

1. A bounded family of defects in a **terminal physical word** may be paid
   once and forgotten.
2. Only the auxiliary state used to construct the next odd dimension has to
   regenerate.  The terminal common-cap compiler, and any terminal holes it
   leaves, do not have to be transported to the next dimension.

Consequently the weakest statement in the present Pascal/RSB framework is
not left-total zero-defect RSB.  It is the existence of one compatible
infinite odd spine whose odd and even terminal physicalizations have
uniformly bounded repair charge, and whose auxiliary sidecar state remains
in a bounded invariant set.

This note proves that statement implies a uniform additive constant.  It
also gives a quantitative contraction criterion.  If a nonnegative carried
defect potential satisfies

\[
                  \Phi(g')\le \rho\Phi(g)+\beta,
                  \qquad \rho<1,
\]

and terminal cost is at most `a Phi+b`, then one may take explicitly

\[
 C=\left\lceil
       a\max\left\{\Phi(g_0),\frac{\beta}{1-\rho}\right\}+b
    \right\rceil .
\]

There is an analogous weighted matrix criterion below.

The currently proved owner transitions do not meet this hypothesis.  The
new connected `K17` factor has zero middle-owner and lower-`q1` defect, but
its canonical physical zipper still has `2392` residence defects and
`1900+911+128=2939` upper holes before the common-cap row.  No uniform bound
on the regenerated compiler state is known.  Thus the theorem below gives
the exact weaker target for `B+O(1)`, not a new unconditional upper bound.

The ordinary closed top-bit splice cannot be that target: even from an
exact odd parent its excess is

\[
             2d_{2m-1}-d_{2m}\in\{d_{2m},d_{2m}+2\}
             =\Theta(\sqrt m).
\]

An additive-constant proof must therefore recompile both Pascal shores once
at the child scale, as in the facet/staircase architecture, rather than lift
two already compiled parent halos.

## 1. Terminal defects are paid; sidecar defects are carried

Put

\[
 r_k=\left\lceil\frac k2\right\rceil,
 \quad W_k={k\choose r_k},
 \quad B(k)=W_k+d_k,
\]

where `d_k` is the proved monotone-deadline depth.

Consider a chain-aligned physicalization at dimension `k`, of physical
length

\[
                         B(k)+c.
\]

It may be flat or nonflat.  Suppose its exact staircase/common-cap replay
proves every target except a family `H`.  More generally, let `R(H)` be the
minimum length of a nonempty set-valued word whose interval unions include
every member of `H`.  Literal listing gives

\[
                         R(H)\le |H|.                 \tag{1.1}
\]

### Lemma 1.1 (terminal repair)

Such a physicalization gives

\[
                     \nu(k)\le B(k)+c+R(H).          \tag{1.2}
\]

#### Proof

Append a word witnessing `R(H)`.  Every old witness remains in the unchanged
prefix, and every missing target occurs in the appended repair word.  \(\square\)

### Lemma 1.2 (repair complexity and hole count)

For every finite family of distinct targets,

\[
 \left\lceil\frac{\sqrt{8|H|+1}-1}{2}\right\rceil
       \le R(H)\le |H|.                              \tag{1.2a}
\]

Thus bounded repair complexity and bounded literal hole count are equivalent
at the `O(1)` scale, although `R(H)` can give the sharper numerical constant.

#### Proof

A word of length `t` has only `t(t+1)/2` nonempty intervals and therefore at
most that many distinct interval-union values.  This gives the lower bound;
literal listing gives the upper bound.  \(\square\)

### Corollary 1.3 (bounded central defect is enough for `O(1)`)

Let a length-`B(k)+c` physicalization cover every target except `h_mid`
middle-rank masks and a family `H'` from the other ranks.  Then

\[
 \nu(k)\le B(k)+c+h_{mid}+|H'|.                    \tag{1.2b}
\]

In particular, the central Catalan matching/ownership row may itself have
uniformly bounded defect in an additive-constant theorem.  Exact central
ownership is required for the zero-defect formula, but is stronger than
necessary for `B(k)+O(1)`.

#### Proof

Take `H` in Lemma 1.1 to be the disjoint union of the missing middle masks
and `H'`, and append them literally.  \(\square\)

This does not make central debt disappear from a recursion.  If the
auxiliary state is exported, its central/palette defect must be included in
the carried potential and contracted or reset just like residence and
provider debt.  The corollary only says that a bounded terminal central debt
is paid once.

Define the **terminal charge**

\[
                         \tau=c+R(H).                \tag{1.3}
\]

This charge is paid only in the dimension in which the physical word is
used.  It must not automatically be inserted into the auxiliary factor or
occurrence data exported to the next Pascal step.

By contrast, a **carried defect** is any failure of the sidecar state needed
by the next odd construction: an unsealed short-run packet, an absent
protected provider, an unresolved occurrence demand, a socket/path-cover
defect, or another declared regeneration coordinate.  Carried defects are
not repaired by appending terminal letters.  They must be reset, contracted,
or retained inside a bounded invariant state family.

This paid/carried distinction is exact.  A terminal common-cap assignment is
not used by the abstract Pascal owner transition unless it is explicitly
declared as an export.  Conversely, appending a missing target says nothing
about the occurrence-labelled auxiliary factor required at the next step.

## 2. The weakest regenerative statement

Let `G_m` be any declared family of auxiliary odd states on `2m+1`
coordinates.  A state may carry a factor, occurrence choices, protected
providers, sockets, run events and any other data used by the construction.
Let

\[
 \mathcal P_m^{\rm odd}\subseteq G_m\times G_{m+1},
 \qquad
 \mathcal P_m^{\rm ev}\subseteq G_m\times A_{2m+2}
                                                               \tag{2.1}
\]

be the literal odd-child and even-terminal transition relations.  An element
of `A_k` is a defective terminal physicalization and has charge `tau` from
(1.3).  Each odd state `g` also contains, or points to, its own terminal
odd physicalization; denote its charge by `tau_o(g)`.

### Theorem 2.1 (bounded-cost odd-spine theorem)

Suppose there are states

\[
                         g_m\in G_m\qquad(m\ge m_0)
\]

and even children `a_m` such that

\[
 (g_m,g_{m+1})\in\mathcal P_m^{\rm odd},
 \qquad (g_m,a_m)\in\mathcal P_m^{\rm ev},           \tag{2.2}
\]

and

\[
 \sup_{m\ge m_0}\max\{\tau_o(g_m),\tau(a_m)\}\le C. \tag{2.3}
\]

Then

\[
                         \nu(k)\le B(k)+C             \tag{2.4}
\]

for every `k >= 2m_0+1`.

#### Proof

Apply Lemma 1.1 separately to the terminal odd physicalization in `g_m` and
to `a_m`.  Equation (2.2) is used only to continue the auxiliary odd spine.
No terminal charge is added to a later dimension.  Taking the uniform bound
(2.3) proves (2.4).  \(\square\)

Within this declared recursive architecture, (2.2)--(2.3) is the weakest
literal sufficient statement: one compatible infinite path is enough.
Left-totality on every state in every `G_m` is a stronger, more convenient
induction theorem, but is not logically necessary.

The theorem also explains why a recurrence of numerical word lengths is the
wrong ledger.  If a child is compiled afresh from an auxiliary owner state,
the parent's terminal `c` cells and repair word are absent from the child
length.  Only sidecar state travels.

## 3. A quantitative contraction certificate

The bounded spine in Theorem 2.1 can be certified without naming it in
advance.

### Theorem 3.1 (scalar defect contraction)

Let `Phi:G_m -> R_+` be a nonnegative carried-defect potential.  Assume
absolute constants

\[
 0\le\rho<1,\quad \beta\ge0,\quad
 a_o,a_e,b_o,b_e\ge0                              \tag{3.1}
\]

such that every reachable `g in G_m` has:

1. an odd successor `g'` with
   \[
                   \Phi(g')\le\rho\Phi(g)+\beta;     \tag{3.2}
   \]
2. an even terminal child `a` with
   \[
                   \tau(a)\le a_e\Phi(g)+b_e;        \tag{3.3}
   \]
3. its own terminal charge bounded by
   \[
                   \tau_o(g)\le a_o\Phi(g)+b_o.      \tag{3.4}
   \]

Starting from `g_0`, put

\[
 E=\max\left\{\Phi(g_0),\frac{\beta}{1-\rho}\right\}. \tag{3.5}
\]

Then a compatible spine exists with `Phi(g_m) <= E` for every `m`, and

\[
 \boxed{
 \nu(k)\le B(k)+
 \left\lceil\max\{a_oE+b_o,a_eE+b_e\}\right\rceil .}
                                                               \tag{3.6}
\]

#### Proof

Choose at each step a successor satisfying (3.2).  If `Phi(g)<=E`, then

\[
 \Phi(g')\le\rho E+\beta\le E,
\]

so induction keeps the whole spine in the sublevel set.  Equations
(3.3)--(3.4) and Theorem 2.1 give (3.6).  \(\square\)

The same proof works if (3.2) is supplied only in expectation by a
distribution on legal successors: some successor is no worse than the
mean.  It also works at the noncontractive endpoint `rho=1,beta=0`, with
`E=Phi(g_0)`.  What does not suffice is a passive estimate

\[
                         \Phi(g')\le\Phi(g)+\beta,
                         \qquad \beta>0,              \tag{3.7}
\]

which yields only a linearly growing upper ledger.  An `O(1)` proof needs a
bounded absorbing set, a nonincreasing potential, or genuine contraction.

### Corollary 3.2 (weighted defect matrix)

Suppose a state has a vector `x(g) in R_+^s`, and legal odd successors can
be selected so that

\[
                         x(g')\le Mx(g)+b             \tag{3.8}
\]

coordinatewise, for one nonnegative matrix `M` and vector `b`.  If there is
`w>0` and `rho<1` with

\[
                         w^T M\le\rho w^T,            \tag{3.9}
\]

put

\[
 E=\max\left\{w^Tx(g_0),\frac{w^Tb}{1-\rho}\right\}. \tag{3.10}
\]

If terminal charges obey

\[
 \tau_o(g)\le q_o^Tx(g)+c_o,
 \qquad
 \tau(a)\le q_e^Tx(g)+c_e,                          \tag{3.11}
\]

then (3.6) holds with

\[
 C=\left\lceil
 \max\left\{
   \left(\max_i\frac{q_{o,i}}{w_i}\right)E+c_o,
   \left(\max_i\frac{q_{e,i}}{w_i}\right)E+c_e
 \right\}\right\rceil .                            \tag{3.12}
\]

#### Proof

Take `Phi=w^Tx`.  Equations (3.8)--(3.9) give

\[
 \Phi(g')\le\rho\Phi(g)+w^Tb.
\]

For nonnegative `x`, `q^Tx <= (max_i q_i/w_i)w^Tx`.  Apply Theorem 3.1.
\(\square\)

This is the precise form in which a finite defect-transfer table would
prove a numerical additive constant.  The table may be dimension-dependent
provided the same `w,rho,b,q,c` bounds work uniformly.

## 4. What the proved Pascal identities do to the defect rows

The natural sidecar vector has at least four qualitatively different rows:

\[
 x=(x_{\rm cent},x_{\rm run},x_{\rm up},x_{\rm comp}),           \tag{4.1}
\]

standing for central owner/palette debt, residence packets, protected
upper-provider debt, and compiler/common-cap debt.  The current mathematics
does not give one finite matrix `M` for all four rows.  It does give the
following exact partial table.

### 4.1 Central ownership and immediate lower colours

A perfect Pascal trace system partitions the two child middle shores
exactly.  A connected integral GMM completion, when supplied, preserves
every immediate lower colour.  Thus on a legal transition

\[
                         x_{\rm cent}=0\longmapsto0.  \tag{4.2}
\]

Perfect Pascal trace systems exist in every dimension.  The connected GMM
completion has been constructed literally at `K15 -> K17`; its uniform
protected version remains open.  Connectivity itself is not necessary when
the downstream braid can order several components.

### 4.2 Residence has an exact one-unit tax

For a parent Johnson trace `C`, put

\[
                         F_i=C_{i-1}\cap C_i.          \tag{4.3}
\]

Every proper positive coordinate run of length `ell>=2` in `C` becomes a
run of length exactly `ell-1` in `F`; singleton runs vanish and all-one
traces stay all one.  Hence, writing `R_[a,b](C)` for the multiset of proper
runs whose lengths lie in `[a,b]`,

\[
                         |R_{[1,d]}(F)|=|R_{[2,d+1]}(C)|. \tag{4.4}
\]

A flat child of depth `d` is residence-clean only when the right side of
(4.4) is zero.  In an odd-to-even step the depth arithmetic is

\[
                         d_{2m}\le d_{2m-1}\le d_{2m}+1. \tag{4.5}
\]

Therefore a depth-drop step `d_(2m-1)=d_(2m)+1` transports ordinary parent
residence for free, while a plateau step `d_(2m-1)=d_(2m)` needs one extra
unit of parent run margin or an explicit nonflat compensation.  This is an
exact propagation law, not a heuristic count.

For the odd diamond branch the same identity applies to each facet shore.
The required margin is always determined by the child threshold through
(4.4), regardless of whether `d` stays constant or increases.  A bounded
number of compensated packets is a valid carried state only if the final
schedule automaton proves that the compensation creates no new short run.

### 4.3 Upper shadows transport internally and fail only at exposed spans

For consecutive parent owners and their facets,

\[
       \bigcup_{j=0}^{q}F_{i+j}
       =\bigcup_{j=0}^{q-1}C_{i+j}.                 \tag{4.6}
\]

Thus every fully internal protected parent occurrence gives both the
unmarked and marked child occurrence at the shifted depth.  After cuts and
joins, the exact cutwise identity is

\[
       \mu'_q(U)=\mu_q(U)-\delta_q^{C}(U)+\eta_q^{J}(U). \tag{4.7}
\]

No bulk upper defect is created.  A target is lost only when every protected
occurrence is exposed and no new seam restores it.  For one cut per source
component, a compatible opening distribution with marginal distortion
`alpha` has expected terminal casualty count at most

\[
 \alpha\sum_i\frac1{|E(Q_i)|}
        \sum_{U\text{ assigned to }Q_i}|B_{Q_i}(U)|. \tag{4.8}
\]

Consequently an absolute bound on (4.8) is already an absolute terminal
upper charge.  It need not be carried if the exported auxiliary child again
has exact protected support.

If an upper hole is merely passed through Pascal without being repaired,
it can have both an unmarked and a marked descendant.  Thus passive support
transport has branching coefficient at least potentially two per added
coordinate, and four across a two-coordinate odd step.  Such a ledger is
not contractive.  The sidecar must retain exact protected support or perform
an explicit reset to a bounded provider state.

### 4.4 The compiler is a reset row

There is no proved functorial map from a parent common-cap assignment to a
child common-cap assignment.  Marginal Hall and scalar surplus do not give
one.  The compiler row must therefore be regenerated at the child after its
chronology and staircase are fixed.  A bounded set of terminal lower holes
may be paid by Lemma 1.1, but those appended cells do not reduce
`x_comp` in the exported auxiliary state.

This is presently the missing entry in any matrix satisfying (3.9).  It is
also why an exact owner factor, even with complete shadow support, does not
by itself prove an additive-constant word theorem.

## 5. Exact obstruction to the closed even splice

Let an odd parent on `2m-1` coordinates have length

\[
                         B(2m-1)+e.
\]

The unconditional top-bit splice has length twice this, and hence excess
over the even lower bound

\[
       e_{\rm ev}=2e+2d_{2m-1}-d_{2m}.              \tag{5.1}
\]

The exact depth dichotomy gives

\[
 2d_{2m-1}-d_{2m}\in\{d_{2m},d_{2m}+2\},            \tag{5.2}
\]

while

\[
                         d_k=\sqrt{\pi k/8}+O(1).    \tag{5.3}
\]

### Proposition 5.1 (closed-splice `O(1)` no-go)

No induction using the unmodified closed top-bit splice as its even
transition can prove `nu(k)<=B(k)+C` with one absolute `C`, even if every odd
parent is exact.

#### Proof

Set `e=0` in (5.1).  Equations (5.2)--(5.3) make the child excess unbounded.
\(\square\)

The obstruction is architectural, not a no-go for even words.  The
facet/staircase transition avoids (5.1) by constructing the complete child
owner layer first and applying one child compiler of depth `d_(2m)`.  In the
defect language, it is a **reset transition** rather than a duplication of
the parent's physical halo.

## 6. Calibration at `K17`

The authenticated `OPTIMAL28` construction now gives one connected cycle on
all

\[
                         {17\choose9}=24310
\]

rank-nine owners, with all `24310` rank-eight consecutive intersections
exactly once.  Hence its central row in (4.1) is zero.

Cutting at the marked/complement crossings and applying the canonical
two-bank zipper gives a prospective row of length `W+1`, with enough scalar
room for a length-`B(17)=W+3` physical word.  Literal replay nevertheless
finds

\[
 \begin{array}{c|c}
 \text{strict short runs for exact D2 inversion}&2392\\
 \text{upper holes at ranks 10,11,12}&1900,911,128\\
 \text{upper holes at ranks 13 through 17}&0.
 \end{array}                                                   \tag{6.1}
\]

The common-cap row has not yet been reached.  The six occurrence swaps and
the `OPTIMAL28` marked packet prove that a large local residence debt can be
reset to zero inside the marked bank.  The fixed complementary facet bank
then reintroduces the `2392` defects in (6.1).  Therefore the finite result
is evidence for a reset mechanism, but it is not a bounded-defect child and
does not supply numerical constants for Theorem 3.1.

## 7. Exact missing bounded-defect theorem

The following is the weakest convenient all-dimensional construction
statement exposed by the audit.

### Bounded-defect sidecar RSB

There exist absolute constants `c,r,E`, one compatible odd spine `g_m`, and
one nonnegative carried potential `Phi(g_m)<=E`, such that for every `m`:

1. the auxiliary odd state has exact middle ownership and a protected
   all-depth provider system suitable for both Pascal children;
2. its odd terminal physicalization has length at most `B(2m+1)+c` and its
   complete upper/lower hole family has repair complexity at most `r`;
3. it has an even facet/staircase child of length at most `B(2m+2)+c`, again
   with repair complexity at most `r`;
4. it has a next odd auxiliary child `g_(m+1)` with `Phi<=E`; and
5. every schedule, upper witness and common-cap assertion in Items 2--3 is
   evaluated jointly on the same literal chronology.  Separate marginal
   witnesses are not allowed.

### Corollary 7.1

Bounded-defect sidecar RSB implies

\[
                         \boxed{\nu(k)\le B(k)+c+r}  \tag{7.1}
\]

in every sufficiently large dimension.

#### Proof

This is Theorem 2.1 with `C=c+r`.  \(\square\)

For exact equality set `c=r=0`.  For an explicit additive constant, it is
enough instead to prove the scalar or matrix hypotheses of Section 3; the
constant is then (3.6) or (3.12).

What remains open is not the implication.  It is one uniform reset theorem
which simultaneously controls the residence row, the protected upper
provider row, and the child common-cap row.  The central owner/q1 theorem and
the closed even splice each omit at least one of those rows.

## 8. Relation to the exact RSB theorem

The exact RSB theorem is recovered by taking zero terminal charge and a
zero carried potential.  The bounded-defect theorem is strictly weaker:

* the terminal compiler may omit a bounded repair family;
* a bounded number of upper targets may be casualties of the selected
  openings;
* the terminal physical word need not itself encode the next auxiliary
  state; and
* only one compatible infinite spine is required.

The following requirements are not weakened, because weakening them without
a reset makes defect grow under Pascal branching:

* exact child middle ownership;
* one literal chain-aligned schedule for each terminal word;
* joint, rather than marginal, cap feasibility for every nonomitted lower
  target; and
* a bounded invariant exported provider/residence/socket state.

This is the sharp present separation between the exact conjecture and the
additive-constant conjecture.
