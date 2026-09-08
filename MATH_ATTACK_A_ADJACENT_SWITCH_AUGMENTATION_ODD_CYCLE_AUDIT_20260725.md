# Adjacent-switch augmentation: the exact implication graph and an odd-cycle obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Verdict

At the level of hypotheses actually supplied by exchange survival—ambient
retained density, local switch cubes, and commuting rectangles—the
following proposed inference is false, even before any asymptotic loss is
present:

> an omitted tag whose adjacent-switch cube retains vertex density
> \(1-m^{-4+o(1)}\), together with intact geodesic switch squares, must
> admit an alternating augmentation into the current matching.

After contracting every switched vertical flag column to one binary
option, and retaining a full product cube (or a feasible face encoded by
unit clauses), the exact simultaneous augmentation problem is a
\(2\)-SAT problem. An arbitrary dense retained subset of a cube need not
have a \(2\)-CNF membership description. In the product case its
alternating exchange graph is the implication graph. The
minimal obstruction is a contradictory implication core, and an odd cycle
of inequality constraints gives such a core.

There is an explicit three-tag example with all of the following
properties.

1. Every tag retains its entire \(d\)-dimensional adjacent-switch cube;
   its retained density is \(1\), and every formal contracted switch
   square is intact.
2. Omitting any one tag leaves a collision-free selection on the other two
   tags.
3. No simultaneous reassignment of any switch bits permits the omitted tag
   to be added.

Thus local cube survival does not force augmentation. A positive theorem
must use additional physical geometry which rules out, or charges, the
contradictory implication cores.

The obstruction is not confined to an arbitrary abstract incidence
matrix. Theorem 3.5 gives a five-bit linear contradictory core realized by
literal local saturated-chain option rails, with actual nested priorities
exposing all six collision targets, no repeated tag pair, and no local
four-antichain conflict. What is not proved is its simultaneous extension
to complete global return-free PBBS trajectories without new protected
collisions. Thus the audit refutes the proposed **local-to-augmentation
inference**, not the existence of a stronger global catalogue theorem and
not the fully global PBBS augmentation statement.

There is a second independent qualification. The proved
\(1-m^{-4+o(1)}\) density is a **tag-fibre average** over a disjoint union of
switch cubes. It need not hold in a particular cube subfibre selected by
owner or priority conditioning. Even if the odd-cycle problem were
removed, a conditional subfibre theorem would still be needed.

## 0A. Exact four-antichain quarantine ledger

Here is the complete numerical gain from the proposed choice. Let
\(A\) be the raw catalogue degree of one calibrated tag fibre, let
\(\mathcal S\) be any already selected family of at most
\(T=(1+o(1))W/g\) chunks, and let \(B_4\) join two chunks on distinct tags
when their protected intersection contains a four-antichain. The audited
raw estimate is

\[
 \Delta(B_4)\le \xi_4 A,
 \qquad \xi_4=m^{-5+o(1)}.
\tag{0.1}
\]

Moreover, one chunk belongs to at most

\[
 K\le g(2Q+1)
\tag{0.2}
\]

protected target-occurrence fibres. Quarantine all neighbours in
\(B_4\) of \(\mathcal S\), and call a fibre exceptional when it loses more
than an \(\eta\)-fraction of its raw catalogue. Double counting the
forbidden chunk incidences gives, for every \(\eta>0\),

\[
 E_{\rm tag}\le (1+o(1)){W\xi_4\over\eta},
 \qquad
 E_{\rm target}\le (1+o(1)){WK\xi_4\over g\eta}.
\tag{0.3}
\]

Indeed, at most \(T\xi_4A\) chunks are forbidden. Each exceptional tag
contains more than \(\eta A\) of them, and its physical weight is \(g\).
For targets, count pairs consisting of a forbidden chunk and a protected
target-occurrence fibre containing it; (0.2) bounds this incidence count
by \(KT\xi_4A\), while every calibrated exceptional target contributes
\((1-o(1))\eta A\).

With the proposed

\[
 \eta=m^{-4},
\tag{0.4}
\]

(0.3) becomes

\[
 \boxed{E_{\rm tag}\le Wm^{-1+o(1)}}
\tag{0.5}
\]

and, when \(Q=m^{1/2+o(1)}\),

\[
 \boxed{E_{\rm target}
 \le W(2Q+1)m^{-1+o(1)}
 =Wm^{-1/2+o(1)}.}
\tag{0.6}
\]

Both are \(o(W)\). The exact quantifier is: for every admissible current
family \(\mathcal S\), there is an \(\mathcal S\)-dependent exceptional
family satisfying (0.5)--(0.6). This is deterministic and does not assume
a random residual. It does not produce one exceptional family valid
simultaneously for every adaptive history, and the bounds may not be
summed over a tree of histories. Nor does it control bad pairs chosen
simultaneously in a new bite; that requires the separate current-bite
bad-edge mass.

For every nonexceptional protected target fibre, raw and retained degrees
satisfy

\[
 d_A(x)\ge(1-\eta)d_0(x),
 \qquad d_A(x,y)\le d_0(x,y).
\tag{0.7}
\]

Consequently, when both \(x\) and \(y\) are nonexceptional, their
normalized pair kernel grows by at most \((1-\eta)^{-1}\). A pair-square
sum restricted to the nonexceptional target block grows by at most
\((1-\eta)^{-2}=1+O(m^{-4})\). The contribution involving exceptional
targets is not covered by this denominator comparison and must be charged
to its separate physical ledger.

## 0B. Exact cube-survival consequences

First suppose that a good fibre is one cube \(Q_k\), with
\(k=\Theta(m)\), and that its deleted set \(B\) has
\(|B|\le\eta2^k\). If \(A=Q_k\setminus B\), directed-edge counting gives

\[
 {1\over|A|}\sum_{x\in A}
 \bigl|\{i:x\oplus e_i\in B\}\bigr|
 \le {k\eta\over1-\eta}.
\tag{0.8}
\]

More generally, the fraction of \(x\in A\) whose complete radius-\(r\)
cube ball is not retained is at most

\[
 {\eta\over1-\eta}\sum_{j=0}^{r}{k\choose j}.
\tag{0.9}
\]

For \(\eta=m^{-4}\) and \(k=\Theta(m)\), the right side is respectively
\(m^{-3+o(1)},m^{-2+o(1)},m^{-1+o(1)}\) for \(r=1,2,3\). At \(r=4\) it
is only \(O(1)\); the quarantine does not prove complete radius-four
survival.

There are two dimensions in the physical catalogue. The full formal
adjacent-switch cube has \(k=\Theta(m)\), as above. After absorbing the
switches which do not change the emitted chunk into the cube index, the
active exchange cube has

\[
 d_{\rm eff}=O(g)\le m^{1/2+o(1)}.
\tag{0.9a}
\]

Applying (0.9) with \(d_{\rm eff}\) shows that every fixed radius
\(r\le7\) active exchange ball survives around all but at most an
\(m^{-4+r/2+o(1)}\) fraction of schedules. In particular, the
radius-one exceptional fraction is \(m^{-7/2+o(1)}\). At \(r=8\) this
argument again gives only \(O(1)\). Thus the strongest unweighted local
conclusion from the proposed parameters is radius seven in the
physically active cube, not an unbounded augmenting radius.

Fixed-dimensional faces behave better. A deleted vertex lies in
\({k\choose t}\) \(t\)-faces, while \(Q_k\) has
\(2^{k-t}{k\choose t}\) such faces. Hence

\[
 {\#\{t\hbox{-faces meeting }B\}
  \over 2^{k-t}{k\choose t}}
 \le 2^t\eta.
\tag{0.10}
\]

In particular, almost every fixed \(t\)-face, including almost every
switch square, is wholly retained. A second double count shows that all
but at most

\[
 \sqrt{2^t\eta}
\tag{0.11}
\]

of the ambient vertices lie in a proportion at least
\(1-\sqrt{2^t\eta}\) of intact \(t\)-faces. Formula (0.11) still tends to
zero uniformly for \(t\le(4-\varepsilon)\log_2m\).

Equations (0.8)--(0.11) extend after averaging over a disjoint union
\(\Omega\times Q_k\). They are ambient statements. They do not imply
the same bounds after owner, priority, or collision-history conditioning;
Section 4 gives the exact obstruction to that inference. Moreover, a
typical formal \(t\)-face may use switches outside the emitted chunk. A
physical exchange-face conclusion requires the labelled-multiplicity
partition into effective cubes and must apply the same incidence count
inside that partition; it is not a conclusion about the simple-support
quotient after duplicate schedules are collapsed.

## 0C. What the exchange-deficient colouring does and does not prove

There is a further unconditional unweighted reduction. In a good tag fibre
with catalogue degree \(D\), call a retained schedule deficient when more
than \(ak\) of its formal switch neighbours were quarantined. Equation
(0.8) and Markov give the tagwise bound

\[
 {|\mathcal E_{\rm def}\cap\mathcal C_U|\over D}
 \le \beta:={\eta\over a(1-\eta)}.
\tag{0.12}
\]

This statement uses the cube whose \(k\) coordinates are being counted.
For the full formal cube, most coordinates may be dummy outside the
emitted chunk, so formal nondeficiency is not by itself physical exchange
richness. An active conclusion must apply the count in the effective-cube
partition while retaining labelled multiplicities.

Declare a protected target additionally exceptional when it occurs in
more than \(\tau D\) deficient candidates. Since each candidate has at
most \(K\) protected targets, double counting deficient
candidate--target incidences gives

\[
 E_{\rm def,target}
 \le {K\beta T\over\tau}
 =O\!\left({Q\beta\over\tau}W\right).
\tag{0.13}
\]

After deleting every adjacency generated by those exceptional target
constraints, the line graph of the resulting **reduced** deficient
candidate hypergraph has maximum degree at most

\[
 (K+1)\max\{\beta,\tau\}D,
\tag{0.14}
\]

so greedy colouring uses at most one plus (0.14) colours.

For the four-antichain parameters choose

\[
 a=m^{-1},\qquad
 \beta=m^{-3+o(1)},\qquad
 \tau=m^{-3/2}.
\tag{0.15}
\]

Then

\[
 \boxed{E_{\rm def,target}=Wm^{-1+o(1)}=o(W)}
\tag{0.16}
\]

and the reduced conflict graph uses

\[
 \boxed{m^{-1/2+o(1)}D=o(D)}
\tag{0.17}
\]

colours.

This is not a proper colouring theorem for the original deficient
hypergraph. One exceptional target may contain \(D\) deficient candidates
on distinct tags. Those candidates form a \(D\)-clique in the original
line graph, although deleting that one target constraint makes the reduced
graph edgeless. The count (0.16) alone neither deletes all candidates in
such stars at small physical cost nor colours those stars with \(o(D)\)
colours. A genuine cleanup still needs a candidate-incidence charge, a
separate literal repair of exceptional targets, or a bound on their
selected duplicate excess.

Thus (0.12)--(0.17) isolate a sparse exceptional-target obstruction but do
not by themselves reduce the literal unweighted matching problem to an
exchange-rich core. Even if that obstruction is repaired, Theorem 3.2
shows that perfect exchange richness is compatible with an integral
odd-cycle defect.

In the common physical repair normalization, the union of all explicitly
counted fibre ledgers in Sections 0A and 0C has weight

\[
 Wm^{-1+o(1)}+Wm^{-1/2+o(1)}+Wm^{-1+o(1)}
 =\boxed{Wm^{-1/2+o(1)}}.
\tag{0.18}
\]

This is again per fixed history \(\mathcal S\). It excludes the unresolved
incidence mass inside the exceptional stars and the separate bad-pair
mass created simultaneously within a new bite.

## 1. The contracted binary-column system

Let \(\mathcal T\) be a finite tag set. For every switch bit \(e\), let

\[
 C_e^0,\ C_e^1
\tag{1.1}
\]

be its two possible protected vertical columns. Targets not controlled by
any switch are called fixed occurrences. Normalize (1.1) by treating a
target common to both \(C_e^0\) and \(C_e^1\) as fixed; hence only the
orientation-dependent part remains in (1.1).

An assignment \(x\in\{0,1\}^{\mathcal E}\) selects \(C_e^{x_e}\) for every
switch bit. It is **simple** if no protected target has two selected
occurrences. Internal exact rainbowness of one trajectory ensures that a
collision is always between two different switch columns, or between a
switch column and a fixed occurrence. A repeated fixed occurrence is an
immediate, assignment-independent obstruction.

For a state \(e^b\), read \(e^b\) as the proposition \(x_e=b\). The
collision of \(C_e^b\) and \(C_f^c\) forbids their simultaneous selection
and gives the clause

\[
 \neg(e^b\wedge f^c),
 \qquad\text{equivalently}\qquad
 e^{1-b}\vee f^{1-c}.
\tag{1.2}
\]

A collision of \(C_e^b\) with a fixed occurrence gives the unit clause

\[
 e^{1-b}.
\tag{1.3}
\]

Parallel target collisions are retained as parallel clause weights when
one minimizes collision excess. For the zero-collision augmentation
question only their support matters.

### Theorem 1.1 (exact binary-column reduction)

Assume there is no fixed--fixed collision. The selected vertical columns
are simple if and only if the switch assignment satisfies every clause
(1.2)--(1.3).

#### Proof

If an assignment violates (1.2), it selects the two occurrences of the
target which generated that clause. If it violates (1.3), it selects the
orientation colliding with the fixed occurrence. Hence simplicity implies
clause satisfaction.

Conversely, every possible repeated target is of one of these two forms
after the common-to-both normalization. Satisfaction of all corresponding
clauses excludes every repetition. \(\square\)

This theorem applies to a collection of full adjacent-switch cubes: all
bits of one tag are assigned simultaneously, so the assignment is one
literal trajectory in that tag's cube. It does not split a vertical flag
column into independent ranks.

## 2. The alternating exchange graph

Define the directed graph \(\mathfrak I\) on the two states \(e^0,e^1\) of
every switch bit. A binary collision (1.2) inserts the two arcs

\[
 e^b\longrightarrow f^{1-c},
 \qquad
 f^c\longrightarrow e^{1-b}.
\tag{2.1}
\]

A unit obstruction (1.3) inserts

\[
 e^b\longrightarrow e^{1-b}.
\tag{2.2}
\]

The meaning of (2.1) is exactly alternating exchange: after choosing
orientation \(b\) at \(e\), a conflicting orientation \(c\) at \(f\) must
be replaced by \(1-c\). Reachability records all forced changes. A
geodesic square says that two independent local bit flips commute inside
one tag cube. It does not delete either implication in (2.1), and it does
not prevent the forced changes from returning with opposite parity.

### Theorem 2.1 (exact contradictory-core criterion)

There is a simple simultaneous switch selection if and only if no switch
bit \(e\) has \(e^0\) and \(e^1\) in one strongly connected component of
\(\mathfrak I\).

#### Proof

Every arc is a logical implication of a clause in Theorem 1.1. If
\(e^0,e^1\) lie in one strongly connected component, choosing either state
forces the other, so no assignment exists.

Conversely, contract the strongly connected components and choose a
topological order in which every arc points forward. Complementation of
states reverses implications: an arc \(A\to B\) is paired with
\(\overline B\to\overline A\). Since no component equals its complement,
declare a component true exactly when it occurs later than its complementary
component. If a true component \(A\) had an arc to a false component
\(B\), the topological order and the complementary arc would give

\[
 A\le B<\overline B\le\overline A,
\]

contradicting that \(A\) occurs later than \(\overline A\). Thus every
implication from a true state has true head, and the resulting assignment
satisfies all clauses. Apply Theorem 1.1. \(\square\)

For a prescribed initial literal \(\ell\), the exact forced-closure
obstruction is already a directed path
\(\ell\leadsto\overline\ell\); equivalently, add the unit clause fixing
\(\ell\) and apply Theorem 2.1. Without a prescribed literal, global
unsatisfiability is mutual reachability of some state and its complement.
In general the closure branches, so an ordinary single augmenting path is
not the correct object; the implication core is. Even satisfiability
supplies a simultaneous reassignment, not automatically an ordering of
one-bit moves whose every intermediate state is simple.

## 3. A full-cube odd-cycle obstruction

It is enough to use three tags \(0,1,2\). Give every tag a full cube

\[
 Q_d=\{0,1\}^d,
 \qquad d\ge1,
\tag{3.1}
\]

and let \(y_i\) be the first switch bit of tag \(i\). The remaining
\(d-1\) bits are completely free and affect only private targets.

For each edge \(ij\in\{01,12,20\}\) and each \(b\in\{0,1\}\), introduce a
target \(a_{ij}^b\). Put \(a_{ij}^b\) in the \(b\)-option column at both
endpoints \(i,j\), and nowhere else. All other target occurrences are
private. If desired, place the three edge families in three different
protected ranks, so that each vertical column still contains at most one
target in any fixed rank.

The two targets on edge \(ij\) give exactly

\[
 y_i\ne y_j,
\tag{3.2}
\]

because \(a_{ij}^0\) forbids \(00\) and \(a_{ij}^1\) forbids \(11\).

### Proposition 3.1 (odd-cycle failure of augmentation)

The system (3.1)--(3.2) has no simple selection on all three tags, but it
has a simple selection after any one tag is omitted.

#### Proof

On all three tags, (3.2) would give

\[
 y_0\ne y_1,\qquad y_1\ne y_2,\qquad y_2\ne y_0,
\]

which is impossible. If tag \(0\) is omitted, choose \(y_1=0,y_2=1\);
the sole remaining constraint is satisfied. The other omitted-tag cases
are symmetric. \(\square\)

The triangle can be blown up without losing any of the degree, capacity,
or cube hypotheses.

### Theorem 3.2 (capacity-perfect full-cube odd-cycle obstruction)

For every odd \(n=2r+1\ge3\) and every \(d\ge1\), put
\(D=2^d\). There is a candidate hypergraph with \(n\) tags such that:

1. the \(D\) candidates above every tag form a complete labelled
   adjacent-switch cube \(Q_d\);
2. every tag has degree \(D\), every protected target has degree at most
   \(D\), and distinct-tag candidates intersect in at most one protected
   target;
3. the uniform point \(z_e=1/D\) saturates every tag and respects every
   target capacity;
4. the four-antichain conflict graph \(B_4\) is empty, all formal switch
   faces and contracted-column rectangles are intact, but a matching covers at most
   \(n-1\) tags;
5. a matching covering exactly \(n-1\) tags exists after any prescribed
   tag is omitted.

Thus a maximum matching has an omitted tag but no augmenting path of any
length, even though the retained cube density is exactly one.

#### Proof

Index the tags cyclically by \(i\in\mathbb Z/n\mathbb Z\), and index the
candidates above tag \(i\) by

\[
 e_{i,\omega},\qquad \omega\in\{0,1\}^d.
\tag{3.5}
\]

Every \(e_{i,\omega}\) contains the tag vertex \(\tau_i\). For every cycle
edge \(i(i+1)\) and \(b\in\{0,1\}\), introduce a protected target
\(a_i^b\), and put it in precisely the candidates

\[
 \{e_{i,\omega}:\omega_1=b\}
 \ \cup\
 \{e_{i+1,\omega}:\omega_1=b\}.
\tag{3.6}
\]

For each dummy coordinate \(2\le j\le d\), one may additionally introduce
targets \(p_{i,j}^b\), present precisely when \(\omega_j=b\). They make
every formal cube coordinate a literal two-column switch and create no
cross-tag collision.

The tag vertex \(\tau_i\) has degree \(D\). Each \(a_i^b\) has degree
\(D/2+D/2=D\), and each \(p_{i,j}^b\) has degree \(D/2\). Two candidates
on distinct tags intersect only when their tags are adjacent and their
first bits agree, in which case their intersection is the singleton
\(\{a_i^b\}\). Hence no distinct-tag pair shares a four-antichain and
\(B_4\) is empty.

Under \(z_e=1/D\), every tag load is \(1\), every \(a_i^b\)-load is
\(1\), and every \(p_{i,j}^b\)-load is \(1/2\). Thus the exact fractional
capacities hold. The whole \(Q_d\) is present at each tag, so every formal
switch edge, square, and higher face is present. Incidence in the switch
bits has the fixed-column plus selected-option-column form, so each
two-coordinate face is a contracted Boolean column rectangle. This
sentence does not assert a literal PBBS arrival-diamond realization.

In an integral matching at most one candidate can be selected above each
tag because of \(\tau_i\). If candidates are selected above both \(i\)
and \(i+1\), (3.6) forces their first bits to differ. A matching covering
all tags would therefore two-colour the odd cycle, which is impossible.
So at most \(n-1\) tags are covered. After omitting any prescribed tag,
the remaining cycle edges form a path; alternate the first bits along
that path and choose the dummy bits arbitrarily. This covers \(n-1\)
tags and proves sharpness. \(\square\)

At the contracted level, the three edge-colour classes of a proper
edge-colouring of the odd cycle may be placed in three abstract rank
slots. At each tag its two incident anchors then occupy different slots
of the same selected column. Thus every separate-slot constraint graph is
a matching; the obstruction comes only from the common column choice.
This rank colouring is not a proof that the slots form one nested physical
flag.

At the two-option quotient, write \(a_{i,b}\) for the mass choosing first
bit \(b\) above tag \(i\). The visible capacity system is

\[
 a_{i,0}+a_{i,1}\le1,\qquad
 a_{i,b}+a_{i+1,b}\le1.
\tag{3.7}
\]

The fractional point \(a_{i,0}=a_{i,1}=1/2\) satisfies every inequality
in (3.7) at equality. Every integral feasible point satisfies the
additional odd-cycle stable-set (blossom-type) inequality

\[
 \boxed{\sum_{i\in\mathbb Z/n\mathbb Z}\sum_{b=0}^1 a_{i,b}\le n-1.}
\tag{3.8}
\]

Inequality (3.8) is not implied by the fractional tag and target
capacities (3.7). Switches in coordinates \(2,\ldots,d\) move inside a
half-cube and the first-coordinate switch crosses between the two
half-cubes; neither local direction manufactures the missing global cut.

Taking a disjoint union of these gadgets preserves all assertions. Taking
\(n\to\infty\) through odd values makes the omitted-tag proportion
\(1/n=o(1)\) while every maximum matching still has one locally
unaugmentable omitted tag in each component.

Theorem 3.2 is deliberately a theorem about the contracted column system.
Complete arrival-diamond supports have an additional nested-chain
restriction.

### Proposition 3.3 (two option clauses force a fixed common base)

Let \((A_u)_u\) and \((B_u)_u\) be saturated nested base chains, with
\(u<v\) implying \(A_u\subset A_v\) and \(B_u\subset B_v\). Let
\(a_0,a_1\) be distinct labels absent from every \(A_u\), and let
\(b_0,b_1\) be distinct labels absent from every \(B_u\). Suppose that,
for some permutation \(\sigma\in S_2\) and some ranks \(r,s\),

\[
 A_r+a_0=B_r+b_{\sigma(0)},\qquad
 A_s+a_1=B_s+b_{\sigma(1)}.
\tag{3.9}
\]

Then \(A_u=B_u\) for at least one \(u\in\{r,s\}\).

#### Proof

If \(r=s\), intersect the two equalities in (3.9). Distinctness and
absence of the arrival labels give \(A_r=B_r\). Suppose \(r<s\). If
\(a_0=b_{\sigma(0)}\), the first equality gives \(A_r=B_r\). Otherwise
that equality forces \(a_0\in B_r\), hence \(a_0\in B_s\) by nestedness.
The right side of the second equality then contains \(a_0\), whereas its
left side does not, because \(a_0\notin A_s\) and \(a_0\ne a_1\). This is
impossible. The case \(s<r\) is symmetric. \(\square\)

Thus two physical arrival diamonds realizing both binary collision
clauses have a common base at a relevant collision rank. If that common
base is a claimed protected source-prefix in the controlled window, then
it occurs in both options of both tags; with complete source-prefix
incidence and total tag mass one it has load two. In particular, under
that complete-incidence hypothesis, the abstract
degree-\(D\), load-one realization of Theorem 3.2 cannot be embedded
unchanged into complete arrival-diamond supports: it acquires a fixed
target of degree \(2D\).

This does not prove a positive augmentation theorem, because the protected
system may hide the forced base by priority. A literal parity
counterexample would have to hide every forced source and endpoint base,
respect the exact rank histogram, avoid all spectator-switch collisions,
and extend to the global return-free trajectory. Conversely, a positive
route must prove that these hiding requirements prevent every large odd
implication core. Neither conclusion follows from cube density or
geodesic rectangles.

Proposition 3.3 has an exact pairwise extension, but that extension still
does not imply satisfiability.

### Proposition 3.4 (two collision cells force a common base)

Under the hypotheses of Proposition 3.3, suppose two distinct cells of
the \(2\times2\) collision matrix between the option pairs
\((a_0,a_1)\) and \((b_0,b_1)\) are realized, possibly at different
ranks. Then the two base chains coincide at one of the two collision
ranks.

#### Proof

Cells in different rows and different columns are Proposition 3.3. Suppose
the cells share the \(A\)-row \(a\):

\[
 A_r+a=B_r+b_0,\qquad A_s+a=B_s+b_1.
\tag{3.10}
\]

They cannot occur at the same rank. Suppose \(r<s\). If \(a=b_0\), the
first equality gives \(A_r=B_r\). Otherwise the first equality forces
\(b_0\in A_r\), hence \(b_0\in A_s\). But the left side of the second
equality contains \(b_0\), while its right side omits \(b_0\), because
both \(b_0,b_1\) are absent from \(B_s\). This is impossible. The case
\(s<r\) is symmetric, and a shared column is the same argument with the
two chains interchanged. \(\square\)

Thus complete protected base incidence permits at most one collision
clause per unordered pair of bits at unit fractional load. The next
construction shows that this pairwise restriction does not eliminate a
contradictory implication core.

### Theorem 3.5 (linear two-crown local physical obstruction)

There are five saturated-chain arrival bits \(X,A,B,C,D\) with the
following properties.

1. Every unordered bit pair supports at most one option-option collision.
2. No two displayed source bases coincide, and no displayed option target
   equals a next-rank source base.
3. The six collision clauses are
   \[
   (\neg x\vee a),\quad(\neg a\vee b),\quad
   (\neg b\vee\neg x),\quad
   (x\vee c),\quad(\neg c\vee d),\quad(\neg d\vee x).
   \tag{3.11}
   \]
   Hence the contracted option system is unsatisfiable, while omitting
   \(X\) leaves a selection on \(A,B,C,D\). Its maximum integral tag
   coverage is exactly four.
4. Under half-option mass, every displayed collision target has load one,
   every displayed fixed source has load one, and every private option
   target has load \(1/2\).
5. The construction is locally compatible with the actual nested
   protected-priority rule and extends each distinguished bit to a full
   formal commuting switch cube. Its local four-antichain graph is empty.

The remaining unproved step is simultaneous extension to five complete
length-\(M\), return-free PBBS trajectories with the exact global
priority histograms and no unintended protected collision at undisplayed
ranks or spectator switches.

#### Proof

Take a core \(K\) and pairwise distinct labels outside it

\[
 x_0,x_1,a_0,a_1,b_0,b_1,f,g,h.
\]

Let the arrival pairs of \(X,A,B\) be respectively
\((x_0,x_1),(a_0,a_1),(b_0,b_1)\). On five consecutive base ranks use
the following saturated fragments:

\[
\begin{array}{c|ccccc}
X&
K+a_0&
K+a_0+f&
K+a_0+f+a_1&
K+a_0+f+a_1+b_1&
K+a_0+f+a_1+b_1+g\\
A&
K+x_1&
K+x_1+b_0&
K+x_1+b_0+f&
K+x_1+b_0+f+h&
K+x_1+b_0+f+h+g\\
B&
K+f&
K+f+a_1&
K+f+a_1+x_1&
K+f+a_1+x_1+g&
K+f+a_1+x_1+g+a_0 .
\end{array}
\tag{3.12}
\]

Each row adds one label at each step and avoids its own two arrival
labels. Write \(V_r^\epsilon\) for the base in row \(V\), column \(r\),
with its \(\epsilon\)-arrival adjoined. Direct comparison of the six
option sets in each column gives exactly

\[
 X_1^1=A_1^0,\qquad
 A_3^1=B_3^0,\qquad
 B_5^1=X_5^1,
\tag{3.13}
\]

and no other cross-row option equality. To make the exhaustion explicit,
after deleting the common core \(K\), the six option sets in columns
\(1,3,5\) are as follows; juxtaposition inside the table denotes the set
of the displayed labels:

\[
\begin{array}{c|cccccc}
1&
a_0x_0&a_0x_1&a_0x_1&x_1a_1&fb_0&fb_1\\
3&
a_0fa_1x_0&a_0fa_1x_1&
x_1b_0fa_0&x_1b_0fa_1&
fa_1x_1b_0&fa_1x_1b_1\\
5&
a_0fa_1b_1gx_0&a_0fa_1b_1gx_1&
x_1b_0fhga_0&x_1b_0fhga_1&
fa_1x_1ga_0b_0&fa_1x_1ga_0b_1 .
\end{array}
\tag{3.14}
\]

The only repetitions in (3.14) are those in (3.13). The six sets in
columns \(2\) and \(4\) are respectively

\[
\begin{array}{c|cccccc}
2&
a_0fx_0&a_0fx_1&x_1b_0a_0&x_1b_0a_1&
fa_1b_0&fa_1b_1\\
4&
a_0fa_1b_1x_0&a_0fa_1b_1x_1&
x_1b_0fha_0&x_1b_0fha_1&
fa_1x_1gb_0&fa_1x_1gb_1 ,
\end{array}
\tag{3.15}
\]

and are all distinct. At each of the five ranks, the three base sets in
(3.12) are pairwise distinct. Comparing each column
of (3.14)--(3.15) with the three bases in the next column of (3.12)
also gives no equality. Notice that placing \(b_1\) before \(g\) in row
\(X\), and \(g\) before \(a_0\) in row \(B\), is needed for the last
comparison.

The equalities (3.13) forbid respectively

\[
 (x,a)=(1,0),\qquad(a,b)=(1,0),\qquad(b,x)=(1,1),
\]

which are the first three clauses in (3.11). Choose a later core \(L\)
containing the final \(X\)-base and neutral fillers but none of the new
arrival labels. Repeat (3.12) with

\[
 (A,B,a_0,a_1,b_0,b_1,x_1,f,g,h)
 \mapsto
 (C,D,c_0,c_1,d_0,d_1,x_0,f',g',h').
\tag{3.16}
\]

The resulting equalities are

\[
 X_1^0=C_1^0,\qquad C_3^1=D_3^0,\qquad D_5^1=X_5^0,
\tag{3.17}
\]

and give the last three clauses of (3.11). The first crown implies
\[
 x=1\Longrightarrow a=1\Longrightarrow b=1
 \Longrightarrow x=0,
\]
so it forces \(x=0\). The second implies
\[
 x=0\Longrightarrow c=1\Longrightarrow d=1
 \Longrightarrow x=1,
\]
so it forces \(x=1\). Thus (3.11) is unsatisfiable.
After omitting \(X\), choose \(a=b=c=d=0\). Neither remaining collision
\((A^1,B^0)\) nor \((C^1,D^0)\) is selected, so four tags are covered.
The maximum integral tag coverage is therefore exactly four, and the
omitted tag has no augmentation inside this local candidate system.

Here is an explicit collision-free gluing of the two fragments. Choose
distinct \(p,q\in K\) and fresh labels
\[
 u,\alpha,\beta,c_0,c_1,d_0,d_1,f',g',h'.
\]
If \(X_5\) denotes the last \(X\)-base in (3.12), put
\[
 L=X_5+u.
\tag{3.17a}
\]
At the single bridge rank take
\[
 X_6=X_5+c_0,\qquad
 A_6=A_5+\alpha,\qquad
 B_6=B_5+\beta,
\tag{3.17b}
\]
\[
 C_6=(L+x_0)-p,\qquad
 D_6=(L+f')-q.
\tag{3.17c}
\]
The next increments are respectively
\[
 u,\quad\hbox{a fresh neutral label for \(A\)},\quad
 \hbox{a fresh neutral label for \(B\)},\quad p,\quad q.
\]
They produce the first bases \(L+c_0,L+x_0,L+f'\) of the second crown
for \(X,C,D\), while the persistent markers \(\alpha,\beta\) keep
\(A,B\) distinct from every second-crown rail and from one another.

It remains to define the earlier prefixes of \(C,D\). For ranks
corresponding to the five columns of (3.12), take nested prefixes of
\[
 C_6=(K-p)+\{a_0,f,a_1,b_1,g,u,x_0\},
\]
\[
 D_6=(K-q)+\{a_0,f,a_1,b_1,g,u,f'\},
\]
adding the seven displayed outside labels in any fixed order. At the
\(j\)-th displayed rank use \(K-p\), respectively \(K-q\), together
with the first \(j+1\) outside labels. Every \(C\)-prefix contains \(q\)
and omits \(p\), while every \(D\)-prefix contains \(p\) and omits \(q\).
All three first-crown bases contain the whole of \(K\). Therefore no
\(C\)- or \(D\)-base or option target can equal a first-crown base or
option target, and no pre-bridge \(C\)-target can equal a pre-bridge
\(D\)-target. The later equality \(C_3^1=D_3^0\) is, of course, one of
the prescribed second-crown collisions. At the bridge rank,
(3.17b)--(3.17c) have the same distinguishing signatures. Direct
comparison with the next three prescribed bases also shows that no bridge
option is a next-rank source base. After the second crown, fresh persistent
markers give an immediate collision-free local continuation.

This proves the claimed local saturated-chain gluing without an
avoidance or randomness assumption. It is not the global return-free
completion asserted as open in the theorem.

Give each distinguished option mass \(1/2\). Every target in
(3.13), (3.17) then receives \(1/2+1/2=1\). The displayed bases are
distinct, so every displayed fixed source receives mass one from one tag;
all other displayed option targets receive mass \(1/2\). Each tag pair
shares at most its single target from (3.13) or (3.17), so the local
\(B_4\) graph is empty.

The preceding fixed-source load refers to complete local incidence. Under
the protected priority truncation below, a hidden fixed source is
unclaimed and has protected load zero.

Each row is a saturated base-chain fragment avoiding its two arrivals.
Extend it locally upward and downward with unused neutral labels and place
the two arrivals in the residual block. The exact two-step
arrival-diamond identity then gives the two intermediate vertical rails
\((C_r+v_0)_r,(C_r+v_1)_r\) with a common source and endpoint. Hence the
displayed rails are literal local arrival diamonds, not merely arbitrary
set columns.

Dummy commuting switches on disjoint local phase blocks preserve the
distinguished half-option marginal and extend each bit to a full formal
cube. If its dimension is \(d\) and \(D=2^d\), every tag has degree
\(D\), every displayed collision target has degree
\(D/2+D/2=D\), and uniform candidate weight \(1/D\) gives the loads just
computed. Since distinct tags share at most one displayed target, internal
\(s=4\) quarantine deletes no cube vertex or local commuting face of the
gadget. For the actual protected priorities, take
\[
 |K|=k=m-Q-1.
\]
The six collision targets then have ranks
\[
 k+2,k+4,k+6,k+8,k+10,k+12,
\]
that is, lower depths \(Q-1,Q-3,\ldots,Q-11\). Let \(c_q\) be the
number of phases claimed at lower depth \(q\). With
\(Q^2/m=\log\log m+\gamma(m)+o(1)\), the central-binomial ratio and
\(MN=(1-o(1))W\) give

\[
 c_Q,c_{Q-11}
 =(1+o(1)){m e^{-\gamma(m)}\over\log m}
 =m^{1-o(1)}=o(M).
\tag{3.18}
\]

Indeed
\[
 {R_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+j+1}
 =\exp\{-q^2/m+o(1)\}
\]
uniformly for \(q\in\{Q-11,Q\}\), while \(W/N=(1+o(1))M\);
the floor in \(c_q=\lfloor R_q/N\rfloor\) is negligible because the
displayed quantity tends to infinity. Give each distinguished
intermediate phase priority at most \(c_Q\), and
its source and common endpoint phases priority greater than
\(c_{Q-11}\). All six intermediate rails are then protected while the
deep source and endpoint shadows are hidden. Mandatory middle owners can
be chosen distinct. This proves local priority compatibility and also
explains why Proposition 3.4 does not remove the core. The unproved global
extension stated in the theorem remains. \(\square\)

At the option-mass quotient of Theorem 3.5, the visible inequalities are
the five tag capacities
\[
 a_{V,0}+a_{V,1}\le1\qquad(V=X,A,B,C,D)
\]
and one two-option target capacity for each forbidden pair in (3.11).
The half point \(a_{V,0}=a_{V,1}=1/2\) satisfies all tag and target
capacities, but every integral point obeys the additional bicycle cut
\[
 \boxed{\sum_{V\in\{X,A,B,C,D\}}\sum_{\epsilon=0}^1
 a_{V,\epsilon}\le4.}
\tag{3.19}
\]
Thus even the one-clause-per-pair physical restriction leaves a genuine
integrality inequality invisible to all marginal capacities and all
local cube faces.

Starting from \(y_1=0,y_2=1\), orientation \(y_0=0\) conflicts with tag
\(1\), while orientation \(y_0=1\) conflicts with tag \(2\). Propagating
the forced flips around the triangle returns to the opposite orientation
of \(y_0\). In \(\mathfrak I\), for each \(b\),

\[
 y_0^b\longrightarrow y_1^{1-b}
 \longrightarrow y_2^b
 \longrightarrow y_0^{1-b},
\tag{3.3}
\]

and the reverse-parity path also exists. Hence the two states of every
active bit lie in one contradictory component.

No cube vertex has been deleted in this example. Therefore every tag has
retained density

\[
 1\ge1-m^{-4+o(1)},
\tag{3.4}
\]

and every formal edge, square, and bounded-radius contracted cube is
intact. The obstruction is cross-tag parity, not local erosion.

The construction is an exact counterexample in the contracted
vertical-column model. The option columns of the triangle do have literal
local saturated-chain realizations, but Proposition 3.3 shows that their
complete arrival-diamond supports then acquire extra fixed-base
collisions and cease to have unit fractional load. It is not known that
priority can hide all those bases while preserving a complete global
physical cube; Theorem 3.5 shows that the nested priority rule can perform
the hiding locally. Consequently the example refutes the deduction from density,
rectangles, and marginal option-column capacities alone; a PBBS-specific
positive theorem could still work by proving that its protected physical
clauses cannot form a large contradictory core.

## 4. Tag-fibre density is not cube-subfibre density

Write one tag fibre as the disjoint union

\[
 \mathcal F=\bigsqcup_{\omega\in\Omega}
             (\{\omega\}\times Q_d),
\tag{4.1}
\]

where \(\omega\) fixes the carrier labelling and all non-switch
decorations. Let \(Z\) be the quarantine deletion set and suppose only

\[
 |Z|\le\eta|\Omega|2^d,
 \qquad \eta=m^{-4+o(1)}.
\tag{4.2}
\]

Put

\[
 z_\omega={|Z\cap(\{\omega\}\times Q_d)|\over2^d}.
\]

Then \(\mathbb E_\omega z_\omega\le\eta\), so for every
\(0<\theta\le1\),

\[
 \boxed{
 {1\over|\Omega|}
 \bigl|\{\omega:z_\omega>\theta\}\bigr|
 \le{\eta\over\theta}.}
\tag{4.3}
\]

This is the strongest deterministic conclusion from (4.2). In
particular, an \(\eta\)-fraction of cube subfibres may be deleted completely.
Owner or priority conditioning may force precisely one of those subfibres.
An average over \(\omega\) cannot then be used at the forced \(\omega\).

There is a sharper denominator trap even inside one ambient cube.

### Proposition 4.1 (high feasible switch degree can be wholly quarantined)

Let \(L=\lceil4\log_2m\rceil\), let \(F\subseteq Q_k\) be a
codimension-\(L\) face, take the pre-quarantine feasible family to be
\(\mathcal A=F\), and take the quarantine set to be \(Z=F\). Then

\[
 {|Z|\over2^k}=2^{-L}\le m^{-4},
\tag{4.4}
\]

every member of \(\mathcal A\) has induced switch degree
\(k-L=k-O(\log m)\), but

\[
 \mathcal A\setminus Z=\varnothing.
\tag{4.5}
\]

#### Proof

A codimension-\(L\) face has \(2^{k-L}\) vertices and is itself a
\((k-L)\)-cube. The displayed assertions follow immediately.
\(\square\)

For example, when \(z=1/\log m\), this \(\mathcal A\) satisfies the
averaged free-switch condition
\[
 2e_{\rm cube}(\mathcal A)/|\mathcal A|=k-L\ge zk
\]
for all large \(m\), yet no feasible candidate survives. Therefore the
comparison “a \(z/2\)-fraction of the current feasible set is rich, while
only an \(m^{-2+o(1)}\)-fraction of ambient vertices is atypical” is
invalid: the two fractions have different denominators. This specifically
invalidates the proposed deduction from an averaged free-switch bound to
an intact feasible face unless one also proves an ambient lower-density
or conditional face-diffusion estimate. High induced dimension alone is
not such an estimate.

The same warning applies along an alternating closure. The next cube
subfibre is chosen by the target conflict created at the preceding step,
so its distribution is history-dependent. To average (4.3) along the
closure one needs either

1. a pointwise lower-density statement on every reachable cube subfibre;
2. a face- or subfibre-diffusion bound conditional on the exchange history;
   or
3. a witness injection charging visits to exceptional subfibres to a
   separate \(o(W)\) ledger.

There is an additional target-fibre issue: toggling a switch changes its
claimed vertical column, so a fixed target fibre need not be a union of
whole cubes. Tag-level cube averaging cannot be silently reused after
conditioning on that target.

## 5. Exact proved and unproved boundary

### Proved

1. Dynamic \(s=4\) quarantine at \(\eta=m^{-4}\) has exceptional
   tag-fibre weight \(Wm^{-1+o(1)}\) and exceptional protected-target
   weight \(Wm^{-1/2+o(1)}\). On the block where both targets are
   nonexceptional it preserves raw denominators with \(1+O(m^{-4})\)
   loss; exceptional-target terms require their own charge.
2. Exchange-deficient schedules have tagwise density \(m^{-3+o(1)}\).
   Another \(Wm^{-1+o(1)}\) target ledger leaves a reduced conflict graph
   colourable with \(m^{-1/2+o(1)}D\) colours. This does not colour the
   original exceptional target stars.
3. In a full-product disjoint adjacent-switch column model, or a feasible
   face encoded by unit clauses, and in the absence of fixed--fixed
   collisions, zero-collision augmentation is exactly \(2\)-SAT.
4. The alternating exchange graph is exactly its implication graph, and
   contradictory strongly connected components are the complete
   obstruction to a simultaneous reassignment.
5. Full formal product cubes, exact fractional capacities, contracted
   rectangles, and empty four-antichain quarantine do not rule out the
   obstruction: every abstract odd-cycle gadget has matching number
   exactly \(n-1\) in tag units.
6. In saturated arrival-diamond geometry, any two collision cells for
   the same unordered bit pair force a common base at a collision rank.
   If that base is protected with complete source incidence, its load is
   two. This proves only one-clause-per-pair, not satisfiability.
7. The explicit five-bit two-crown formula is a linear unsatisfiable
   \(2\)-CNF using every bit pair once. Its option rails have a literal
   local saturated-chain realization, exact local unit loads, locally
   compatible nested priorities, and empty local \(B_4\).
8. A \(1-m^{-4+o(1)}\) tag-fibre density gives only the subfibre Markov
   estimate (4.3), not a statement about a forced cube.

### Still needed for a positive physical augmentation theorem

One must prove at least one genuinely catalogue-specific assertion:

* the implication graph generated by physical vertical-column collisions
  has no contradictory core after deleting \(o(W)\) clause weight,
  equivalently a physical odd-cycle/bicycle cut which supplements the
  marginal tag/target capacities;
* every contradictory core has a fresh geometric witness which can be
  charged to the existing pair-square/bow-tie ledger; or
* an augmentation uses a conditionally diffuse family of cube subfibres
  and avoids both the quarantine exceptional set and all odd implication
  cycles.

The explicit smallest missing **global** lemma is therefore:

> every locally realized linear bicycle core such as Theorem 3.5 either
> fails to extend to complete return-free, exact-priority PBBS trajectories,
> or creates a new protected collision witness chargeable to \(o(W)\).

The density and intact-square statements alone prove none of this.

## 6. Adversarial audit

1. The obstruction uses an implication cycle across tags, not a deleted
   local switch. Strengthening \(1-m^{-4}\) to density \(1\) does not
   repair it.
2. The degree normalization is exact: tag and shared-anchor degrees are
   \(D=2^d\), and the uniform candidate weight \(1/D\) gives load one.
   Thus the obstruction is not caused by a deficient marginal.
3. Dummy bits make the formal cube have arbitrary dimension, including
   \(d=\Theta(m)\), without affecting the contradiction. They do not
   replace useful active switches; the proved active dimension is only
   \(O(g)\).
4. A proper three-edge-colouring places the abstract odd-cycle anchors in
   distinct formal slots, so every slot separately sees a matching. It
   does not construct one nested physical flag.
5. Theorem 3.2 is deliberately contracted. Theorem 3.5 is a literal
   local saturated-chain/protected-column realization, but neither is a
   complete exact-factor counterexample: global return-free completion,
   all shallow protected ranks, and spectator-wide collision avoidance
   remain unproved.
6. The \(2\)-SAT criterion concerns existence of a final simultaneous
   assignment. A sequential one-hole-at-a-time reconfiguration may need
   extra ordering hypotheses even when the formula is satisfiable. No
   such stronger conclusion is claimed.
7. The exceptional-fibre bounds (0.5)--(0.6) hold uniformly at each fixed
   residual family, but they cannot be summed over an adaptive tree of
   histories. The codimension-\(4\log_2m\) example shows why replacing
   this with a conditional claim would be invalid.
8. The \(o(D)\) colouring in Section 0C is only for the graph after
   exceptional-target adjacencies are removed. One exceptional target can
   still induce a \(D\)-clique in the original line graph.
9. The \(2\)-SAT reduction applies to full product cubes or faces encoded
   by unit clauses. An arbitrary dense retained subset introduces an
   additional membership constraint which need not be \(2\)-CNF.
