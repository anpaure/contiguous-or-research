# K17 bounded-q1 fallback: the exact `h=1` occurrence-port master

**Date:** 2026-08-02  
**Status:** proof-safe design and exact reduction.  This note does not claim
SAT, a source word, or `nu(17)=24313`.  It is the first bounded relaxation to
launch only after the exact-q1 circuit descent has genuinely plateaued.

**Selector update.**  The physical-edge variables below are the transparent
semantics, not the implementation target.  The exact augmented-incidence
lollipop theorem in
`MATH_THEOREM_K17_H1_INCIDENCE_EULER_REDUCTION_20260802.md` projects the same
central object to 218,790 containment-incidence variables by replacing the
opened `DB` incidence with the missing boundary incidence `MB`.  The
lollipop selector is authoritative; Sections 3--7 below remain the literal
acceptance interface attached to its Euler chronology.

**Existence update.**  The later theorem
`MATH_THEOREM_ODD_MIDDLE_LEVELS_FIXED_BOUNDARY_LOLLIPOP_EXISTENCE_20260802.md`
constructs this connected fixed-boundary degree core for every odd Middle
Levels graph (and hence for `K17`).  The outer selector is therefore choosing
among a nonempty central family; residence, upper coverage, and the lower
compiler remain genuine simultaneous filters.

## 0. Purpose and scope

Put

\[
 r=9,\qquad d=3,\qquad W=\binom{17}{9}=24310.
\]

The positive-slack q1-rigidity theorem proves that every hypothetical tight
K17 word has at most six rank-eight targets outside its clean Johnson/q1
core, and the path-cover theorem proves that the core has at most six path
components.  Therefore a Catalan-scale relaxation is unjustified.  The
correct fallback is the bounded ladder

\[
                  h=1,2,\ldots,6,                 \tag{0.1}
\]

where `h` counts named exceptional rank-eight top ports and core paths.

This note gives the exact first rung.  It searches a sufficient flat
depth-three face with:

* every rank-nine owner once;
* a cyclic Johnson carrier whose rank-eight edge-colour multiset has one
  missing colour and one duplicated colour;
* one occurrence of the duplicated colour designated as the opening;
* the missing colour installed as one occurrence-labelled boundary top
  port;
* complete upper coverage after the opening;
* zero **internal** residence defect after the chosen opening (short cyclic
  runs stabbed by that opening are clipped and allowed); and
* a literal two-row lower compiler.

The design deliberately breaks `Z_17` equivariance.  A single physical
missing colour cannot be represented by a free rotation orbit of size 17.

The central `h<=6` core/path-cover master in Section 8 is necessary for any
tight word at the two central layers.  The flat `h=1` source face is a
strong, exactly checkable first search class; it is not asserted to be WLOG
for every arbitrary-start/deadline tight word.

## 1. Physical edge catalogue

Let

\[
 \mathcal Q=\binom{[17]}8,\qquad
 \mathcal T=\binom{[17]}9.
\]

For `Q in \mathcal Q` and distinct `a,b notin Q`, let

\[
 e=(Q;a,b)=\{Q+a,Q+b\}.                            \tag{1.1}
\]

This is one undirected Johnson edge between two owners.  Its lower colour
is `Q` and its upper colour is `Q+a+b`.  There are exactly

\[
 |\mathcal Q|\binom92=24310\cdot36=875160          \tag{1.2}
\]

physical edge variables `x_e`.

For every owner `T`, impose

\[
             \sum_{e\ni T}x_e=2.                  \tag{1.3}
\]

Lazy component cuts require the selected two-factor to be one cycle.
Every accepted outer assignment is therefore a Hamilton cycle on all
24,310 owners, not merely a palette factor.

## 2. Exactly one missing and one duplicated lower colour

Introduce `m_Q,d_Q in {0,1}` and impose

\[
 \sum_Qm_Q=1,\qquad \sum_Qd_Q=1,\qquad m_Q+d_Q\le1, \tag{2.1}
\]

and

\[
       \sum_{e:\,q(e)=Q}x_e=1-m_Q+d_Q             \tag{2.2}
\]

for every rank-eight colour `Q`.

Thus one colour has load zero, one has load two, and all others have load
one.  The total is `W`, as required by (1.3).  These are physical colours,
not quotient orbits.

Introduce one opening literal for every selected edge,

\[
                         o_{AB},                    \tag{2.3}
\]

with exactly one opening globally.  Require

\[
 o_{AB}\Longrightarrow x_{AB}\wedge d_{A\cap B}.  \tag{2.4}
\]

Let `M` be the unique colour with `m_M=1`.  The occurrence-labelled port
condition is

\[
 o_{AB}\Longrightarrow (M\subset A\ \text{or}\ M\subset B). \tag{2.5}
\]

It must not be encoded by the quadratic complement of the containment
relation.  Introduce the sparse incidence variables

\[
 p_{M,T}\qquad(M\in\mathcal Q,\ T\in\mathcal T,\ M\subset T), \tag{2.6}
\]

of which there are only `W*9=218790`.  Choose exactly one `p_(M,T)`, imply
`m_M`, and imply that `T` is an endpoint of the unique opening edge.  This is
equivalent to (2.5).  In fact `M` cannot be contained in both endpoints: then
`M=A\cap B`, contradicting `m_M+d_M<=1`.  Hence `M` uniquely orients the
opening.  Call the endpoint containing `M` the initial owner `B`, and the
other endpoint the terminal owner `A`.

The other selected edge incident with `A` must have a lower colour different
from `A\cap B`.  This prevents the final internal root from coinciding with
the terminal boundary root.  It is encoded conditionally on the opening and
the unique missing colour that determines which endpoint is `A`.  A lazy
three-literal blocker is sufficient when a decoded opening violates this
row; enumerating all such triples eagerly is unnecessary.

## 3. The augmented linear coatom path

Decode the opened owner order as

\[
       T_0=B,T_1,\ldots,T_{W-1}=A.                 \tag{3.1}
\]

For `1<=i<W`, put

\[
       Q_i=T_{i-1}\cap T_i.                        \tag{3.2}
\]

These are the selected edge colours other than the opening.  Because the
opening removes one of the two occurrences of the duplicated colour, the
`Q_i` are pairwise distinct and equal to `\mathcal Q\setminus\{M\}`.

Put

\[
       Q_0=M,\qquad Q_W=A\cap B.                   \tag{3.3}
\]

Then

\[
       Q_0\cup Q_1=T_0,\qquad
       Q_{W-1}\cup Q_W=T_{W-1}.                   \tag{3.4}
\]

The first identity follows from `M\subset B`, `Q_1\subset B`, and
`M\ne Q_1`; the inequality is automatic because `M` is absent from all
selected cycle edges.  The second follows from the last clause in Section 2.
Every internal identity is

\[
       Q_i\cup Q_{i+1}=T_i.                        \tag{3.5}
\]

Consequently `Q_0,...,Q_W` is a literal linear Johnson walk whose consecutive
unions are every rank-nine owner exactly once.  Its multiset contains every
rank-eight target once and the duplicated opening colour once more.

This is the exact meaning of the exceptional top port: the missing cyclic
edge colour is inserted as the first physical width-three root, while the
cut duplicated colour becomes the terminal width-three root.

The opposite port is obtained automatically when the unique missing colour
lies in the other endpoint of the chosen opening edge.

## 4. Linear age-run theorem and unmarked source spelling

The cyclic age-run theorem has the following immediate linear form.

### Lemma 4.1 (linear age-run criterion)

Let `Q_0,...,Q_N` be a linear rank-`s` Johnson walk.  There are nonempty
letters

\[
             E_0,E_1,\ldots,E_{N+2}               \tag{4.1}
\]

such that

\[
 Q_i=E_i\cup E_{i+1}\cup E_{i+2}\quad(0\le i\le N) \tag{4.2}
\]

if every internal positive coordinate run in the `Q`-walk has length at
least three, together with a choice of nonempty age-zero, age-one, and
age-two classes at the clipped left root.  Conversely every such spelling
has the same internal-run property.  Boundary runs are clipped and carry no
lower bound.

#### Proof

Apply the coordinatewise proof of the frozen age-run theorem to every
internal run.  At the left boundary choose the ages of already-present
coordinates freely in `{0,1,2}`; at the right boundary no prescribed
departure age is needed.  Refresh choices for distinct coordinate runs are
independent.  Taking each new letter to be the age-zero class gives (4.2).
Nonemptiness at internal positions follows from the newborn coordinate;
the three clipped initial letters are exactly the stated boundary condition.
The converse is the usual oldest-departure argument on an internal run.
\(\square\)

The outer residence oracle therefore replays the augmented path (3.3), not
the uncut cycle alone.  A bad internal run of length one or two gives a
sound local blocker on the selected consecutive physical edges; if it
touches the artificial boundary, the blocker additionally contains the
opening orientation and missing-colour literals.

Once this oracle reports zero, an explicit unmarked depth-three source
spelling exists automatically.  No antecedent SAT claim is still missing at
that point.  What remains is the choice of refreshes compatible with named
lower flags/pins and the literal lower compiler.

## 5. Upper rows after the opening

The opening edge is not an adjacency of the linear owner chronology.  For
every rank-ten target `U`, require

\[
 \bigvee_{e:\,u(e)=U}\bigl(x_e\wedge\neg\operatorname{open}_e\bigr). \tag{5.1}
\]

Tseitin witnesses make (5.1) exact.  It is not sufficient to audit the
uncut cycle.

Ranks 11 through 17 are handled by the fixed-word first-arrival oracle on
the opened owner path.  A miss contributes a certified labelled-frontier
cut when available and otherwise the exact incumbent chronology no-good.
Acceptance requires literal replay of all 21,778 upper targets.

## 6. The lower compiler collapses to two rows

Choose one age spelling from Lemma 4.1.  The width-three source unions are
exactly

\[
                  Q_0,Q_1,\ldots,Q_W,              \tag{6.1}
\]

so every rank-eight target is already present.  Since every width-three
cell has rank eight, no target of rank at most seven can occur first at
width three.  The entire remaining lower compiler is exactly

\[
 \{E_i:0\le i<W+3\}\ \cup\
 \{E_i\cup E_{i+1}:0\le i<W+2\}.                  \tag{6.2}
\]

It has

\[
             (W+3)+(W+2)=2W+5=48625               \tag{6.3}
\]

physical cells for

\[
             \sum_{s=1}^7\binom{17}s=41225        \tag{6.4}
\]

named targets, leaving the exact scalar slack 7400.

For a fixed augmented `Q`-path, encode the age/refresh alternatives from
Lemma 4.1.  A provider for a target `S` is either

\[
 E_i=S\quad\text{or}\quad E_i\cup E_{i+1}=S.       \tag{6.5}

\]

Each equality is a conjunction of 17 literal membership conditions and is
channelled by one lazy Tseitin atom.  Missing targets add only their exact
provider ALO rows.  A final scan of the emitted letters is mandatory; no
rank-only or cell-deletion surrogate is accepted.

This inner model is where named lower flags, pins, and the compiler live.
The frozen age-run theorem removes only the unmarked spelling gate.

### Theorem 6.1 (soundness of an accepted `h=1` instance)

If the opened carrier passes Sections 3--5 and one age spelling satisfies
the provider rows (6.5) for every target of rank at most seven, then
`E_0,...,E_(W+2)` is a universal K17 word of length `W+3=24313`.

#### Proof

Equation (6.1) covers rank eight, and (3.4)--(3.5) cover every rank-nine
owner.  Equation (6.5) covers ranks one through seven.  Every source interval
of length at least four is the union of the consecutive length-four owner
windows it contains; conversely every consecutive owner union is such a
source interval.  Section 5 therefore covers ranks ten through seventeen.
All source letters are nonempty by Lemma 4.1.  These are all 131,071
nonempty targets.  \(\square\)

## 7. Fail-closed solve order

Before lazy connectivity, residence, and deeper-upper rows, the sparse outer
variable census is

\[
 875160\ (x_e)+48620\ (m_Q,d_Q)+875160\ (o_e)
 +218790\ (p_{M,T})=2017730.                       \tag{7.1}
\]

The upper-q1 rows need no per-edge conjunction variables in a pseudo-Boolean
master: because `o_e<=x_e`, their exact form is

\[
 \sum_{e:u(e)=U}x_e-\sum_{e:u(e)=U}o_e\ge1.       \tag{7.2}
\]

The implementation must use the following nested acceptance order.

1. Select the physical cycle, missing/duplicated colours, and oriented
   opening.
2. Enforce owner degree, exact colour loads, upper q1 after the opening, and
   lazy one-cycle cuts.
3. Materialize the augmented coatom path and add exact residence blockers
   until Lemma 4.1 passes.
4. Replay ranks 11--17 on the opened owner path and add certified chronology
   cuts until the complete upper deck passes.
5. Solve the age/refresh inner model with the rank-one-through-seven provider
   rows and the named boundary port fixed.
6. Emit the `W+3=24313` source letters and literally replay all 131,071
   nonzero targets.

An outer carrier is not promoted when only steps 1--4 pass.  An inner UNSAT
for one carrier blocks only that authenticated carrier/opening/port tuple
unless a smaller dependency core is independently proved.  SAT is accepted
only after the final literal replay.

The heavy master belongs on the H100 CPU.  It must use a unique root,
proof/model retention, exact input hashes, and one-heavy-job-at-a-time
resource discipline.

## 8. The theorem-complete bounded central fallback (`h<=6`)

For later rungs, it is cleaner to use the alternating Middle Levels
incidence variables

\[
 y_{Q,T}=1\quad\Longleftrightarrow\quad
 Q\subset T\text{ is a selected core incidence}. \tag{8.1}

For fixed `h`, impose

\[
 \sum_{T\supset Q}y_{Q,T}=2z_Q,\qquad
 \sum_Qz_Q=W-h,\qquad
 \sum_{Q\subset T}y_{Q,T}\le2.                    \tag{8.2}

Lazy cycle cuts make the selected incidence graph acyclic.  It contains all
`W` owners and `W-h` coatoms, with `2(W-h)` incidences, so Euler's formula
gives exactly

\[
 (W+W-h)-2(W-h)=h                              \tag{8.3}

path components.  The `h` colours with `z_Q=0` are the occurrence-labelled
exceptional top-port bank.  There are exactly `2h` free owner endpoint
slots.

Choose `h-1` endpoint-capacitated owner seams whose contracted graph joins
the `h` core paths into one linear chronology.  The seams may be duplicated-
colour Johnson transitions or genuinely non-Johnson transitions.  This
represents all `W-h` forced clean transitions plus at most `h-1<=5`
exceptional transitions from the rigidity theorem.  Assign the `h` missing
coatoms to actual exceptional atlas chains, not abstract labels.

Residence is componentwise, not cyclic, on this general face.  Let every
short positive coordinate run carry the set of old physical cut edges that
would make that run touch a path boundary (the two boundary edges together
with its internal edges).  The selected core cuts must hit every such
support.  Equivalently, the interval-stabbing number of the short-run support
family must be at most `h`.  After cutting, all remaining internal positive
runs have length at least three, so the linear age-run lemma spells every
component.  Demanding zero short runs on the uncut cycle would be strictly
stronger than the theorem-complete `h<=6` target.  This stabbing row is not
by itself a seam certificate: the exceptional interfaces must either keep
the component boundaries physically clipped or pass their own literal
source-state replay; arbitrary joins can create new short internal runs.

Equations (8.1)--(8.3), the exact short-run stabbing row, endpoint-labelled
seams, and literal port assignment are the theorem-complete **central**
bounded fallback: every tight K17 word induces an instance for some `h<=6`.
Source spelling, arbitrary-width upper coverage, and the lower compiler must
still be attached to the same physical chronology.  The `h=1`
Johnson-closure face in Sections 1--7 is the smallest such attachment; its
augmented linear residence test already permits the sole opening to clip
cyclic short runs, and then the frozen age-run theorem gives the unmarked
source spelling.

## 9. Decision ladder

The search order is therefore:

1. exhaust the current exact-q1 length-preserving circuit component;
2. solve `h=1` with a Johnson duplicated-colour closure as above;
3. if necessary, retain `h=1` but allow a non-Johnson artificial closure in
   the central master, with a direct linear source-state oracle;
4. increase `h` one at a time, never beyond six, using (8.1)--(8.3).

No broad lower-q1 relaxation is justified before these bounded faces are
decided.
