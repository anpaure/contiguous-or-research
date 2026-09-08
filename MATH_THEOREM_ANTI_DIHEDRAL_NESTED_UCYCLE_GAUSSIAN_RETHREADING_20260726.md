# Anti-dihedral singleton rigidity and the exact two-rotor rethreading gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom n m .
\]

The positive-density long-endpoint theorem in
`MATH_THEOREM_GAUSSIAN_ANNULUS_LONG_ENDPOINT_RETHREADING_OBSTRUCTION_20260726.md`
shows that a fixed Gaussian annulus cannot be added while retaining almost
all of the short PBBS owner witnesses.  This note audits the most natural
wholesale alternative: a sliding singleton Ucycle with rank-reversing
dihedral symmetry.

The symmetry does make upper-band coverage automatic from lower-band
coverage at **every depth simultaneously**.  But it also forces

\[
                         s_{i+n}=s_i
\]

on every component.  Distinct middle windows then force every component
to have length exactly (n): it is an ordinary wreath.  Consequently an
anti-dihedral singleton factor has exactly (W/n) components and costs a
positive fraction of (W) to linearize.  It cannot be the missing
Gaussian-annulus rethreading.

\[
 \boxed{
 \text{anti-dihedral singleton sliding factor}
 \ \Longrightarrow\
 \text{exactly }W/n\text{ wreath components}
 \ \Longrightarrow\
 \text{linearization excess }(1/2+o(1))W.}
\tag{0.0}
\]

What survives is a sharper positive reduction with the symmetry removed.
Every recurrence-((n-1)) singleton Ucycle factor is an integral
fibre-transversal circulation in a binary rotor graph on (S_n).  Lower
and upper band coverage are explicit prefix inequalities, the component
target is (o(W/m)), and there is an exact common all-rank fractional
solution.  This direct two-sided circulation is the remaining long-endpoint
skeleton theorem.

More precisely, let

\[
 s=(s_i)_{i\in\mathbb Z_W},\qquad s_i\in[n],
\tag{0.1}
\]

be a cyclic word and put

\[
 X_i=\{s_i,s_{i+1},\ldots,s_{i+m-1}\}.
\tag{0.2}
\]

Assume:

1. the (X_i)'s are the (W) members of \(\binom{[n]}m\), each once;
2. for some coordinate permutation (R), the rank-reversing Boolean
   anti-automorphism

   \[
   \theta(A)=[n]\setminus R(A)
   \tag{0.3}
   \]

   satisfies

   \[
   \theta(X_i)=Y_{\epsilon i+c},
   \qquad
   Y_j:=X_j\cup X_{j+1},
   \qquad \epsilon\in\{+1,-1\};
   \tag{0.4}
   \]

3. for every (0\le q\le H), the cyclic windows

   \[
   S_{i,q}:=\{s_i,s_{i+1},\ldots,s_{i+m-q-1}\}
   \tag{0.5}
   \]

   cover \(\binom{[n]}{m-q}\).

Formally, if the hypotheses below held, the linear singleton word obtained by writing one period of (s) and
repeating its first (m+H) symbols has length

\[
 \boxed{W+m+H}
\tag{0.6}
\]

and covers every rank in

\[
 [m-H,m+1+H].
\tag{0.7}
\]

Every rank-(m) set has a selected witness of length (m), every
rank-((m+1)) set one of length (m+1), the lower flags use common left
endpoints, and the upper flags use common right endpoints.  Thus (0.1)--
(0.5) solve the exact long-endpoint rethreading gate, rather than patching
the shallow PBBS witnesses.

However, Theorem 1.3 below shows that these hypotheses force a length-(n)
wreath component.  The following formerly tempting one-sided object is
therefore **impossible with sub-Catalan component count**.

> **Anti-dihedral nested-Ucycle theorem (closed negatively).**  Construct (0.1) with
> (0.2)--(0.5), first for every fixed (H=A\sqrt m), and ultimately for
> some (H/\sqrt m\to\infty), (H=o(m)).

Trace duality makes the upper half redundant, but singleton rigidity makes
every component a wreath, so this formulation cannot have the required
linearization cost.

The useful replacement is Theorems 1.7--1.8 and 2.4 below: impose both
prefix families directly on a non-symmetric binary-rotor circulation.

## 1. Anti-dihedral trace duality in the Middle Levels graph

Let a Middle-Levels Hamilton cycle (or one component of a cycle factor) be
written

\[
 \cdots,X_i,Y_i,X_{i+1},Y_{i+1},\cdots,
 \qquad |X_i|=m,\qquad |Y_i|=m+1.
\tag{1.1}
\]

Necessarily

\[
 Y_i=X_i\cup X_{i+1}.
\tag{1.2}
\]

For (q\ge0), define the backward lower and forward upper traces

\[
 L_{i,q}=\bigcap_{j=0}^{q}X_{i-j},
 \qquad
 U_{i,q}=\bigcup_{j=0}^{q+1}X_{i+j}.
\tag{1.3}
\]

Suppose the cycle is invariant under a rank-reversing coordinate
anti-automorphism (\theta).  On an invariant component, its induced
action on the abstract cycle is dihedral, so after indexing there are
\(\epsilon\in\{+1,-1\}\) and (c) such that

\[
 \theta(X_i)=Y_{\epsilon i+c}.
\tag{1.4}
\]

Here (\epsilon=+1) is the rotational case and (\epsilon=-1) is the
reflection case.

If \(\theta\) is an involution and the component has (L) lower-shore
vertices, the phase is forced.  From adjacency in (1.1),

\[
 \theta(Y_i)=
 \begin{cases}
 X_{i+c+1},&\epsilon=+1,\\
 X_{-i+c},&\epsilon=-1.
 \end{cases}
\tag{1.4a}
\]

Thus the rotational case requires

\[
 \boxed{2c+1\equiv0\pmod L,}
\tag{1.4b}
\]

so an invariant component is odd and (c=(L-1)/2).  The reflection case
has no parity restriction and has two fixed axis edges.  This is why plain
complement can only be rotational, while a reverse-complement involution
with fixed Middle-Levels edges is the natural reflection symmetry.

### Theorem 1.1 (all-depth trace duality)

Under (1.4), for every (i,q),

\[
 \boxed{
 \theta(L_{i,q})=
 \begin{cases}
 U_{i-q+c,q},&\epsilon=+1,\\[1mm]
 U_{-i+c,q},&\epsilon=-1.
 \end{cases}}
\tag{1.5}
\]

Consequently, at every depth where the traces have the intended ranks,
the lower and upper trace-load multisets are identical after applying
\(\theta\).  In particular, lower coverage implies upper coverage, with
exactly the same hole and multiplicity profile.

#### Proof

The map (\theta(A)=[n]\setminus R(A)) reverses intersections and unions.
Therefore

\[
 \theta(L_{i,q})
 =\bigcup_{j=0}^{q}\theta(X_{i-j})
 =\bigcup_{j=0}^{q}Y_{\epsilon(i-j)+c}.
\tag{1.6}
\]

If (\epsilon=+1), the indices on the right are the consecutive interval
from (i-q+c) through (i+c).  By (1.2), its union is the union of the
(q+2) consecutive (X)'s beginning at (i-q+c), namely
(U_{i-q+c,q}).

If (\epsilon=-1), the indices are the consecutive interval from
(-i+c) through (-i+q+c).  Its union is (U_{-i+c,q}).  This proves
(1.5).  Both index maps in (1.5) are bijections, and (\theta) is a
bijection between ranks (m-q) and (m+1+q), proving the load statement.
\(\square\)

This theorem corrects a common depth-indexing confusion.  An immediate
lower colour of rank (m-1) is dual to an upper trace of rank (m+2), not
to the immediate upper colour of rank (m+1).  That is exactly the paired
depth convention required by the Gaussian annulus.

### Corollary 1.2 (symmetry forces the long recurrence gap)

In the sliding-window setting (0.1)--(0.4), every cyclic symbol window of
length at most (m+H+1) is injective.  Equivalently, equal symbols in the
cyclic word have separation at least (m+H+1).

#### Proof

Every lower trace (L_{i,q}=S_{i,q}) has rank (m-q), because it is a
subwindow of an injective (m)-window.  The two index maps in (1.5) are
surjective, so Theorem 1.1 says **every** upper trace (U_{k,q}) has rank
(m+1+q).  By (2.3), these are exactly all cyclic symbol windows of that
length.  Taking (q=H), and then passing to subwindows, proves the claim.
\(\square\)

Thus the anti-dihedral condition pays the entire physical (H)-residence
gate automatically.  It is stronger than merely making the upper target
map surjective.

### Theorem 1.3 (anti-dihedral singleton rigidity)

Assume (m\ge2).  Let one sliding-window component have (L) distinct middle windows and
satisfy (1.4), for either sign \(\epsilon\).  Then

\[
 \boxed{s_{i+n}=s_i\quad(i\in\mathbb Z_L).}
\tag{1.6a}
\]

Consequently (L=n), the (n) symbols in one period are pairwise
distinct, and the component is an ordinary wreath.

#### Proof

The transition (X_i\to X_{i+1}) deletes (s_i) and adds (s_{i+m}).
Applying \(\theta(A)=[n]\setminus R(A)\) reverses these roles: the
transition \(\theta(X_i)\to\theta(X_{i+1})\) deletes (R(s_{i+m})) and
adds (R(s_i)).

First suppose \(\epsilon=+1\), and put (k=i+c).  The corresponding
upper transition is (Y_k\to Y_{k+1}), which deletes (s_k) and adds
(s_{k+m+1}).  Uniqueness of the exchanged coordinates gives

\[
 R(s_{i+m})=s_{i+c},
 \qquad
 R(s_i)=s_{i+c+m+1}.
\tag{1.6b}
\]

Apply the second identity at (i+m) and compare it with the first:

\[
 s_{i+c}=R(s_{i+m})=s_{i+c+2m+1}=s_{i+c+n}.
\]

Now suppose \(\epsilon=-1\), and put (k=-i+c).  The image transition
is (Y_k\to Y_{k-1}), which deletes (s_{k+m}) and adds (s_{k-1}).
Hence

\[
 R(s_{i+m})=s_{k+m},
 \qquad
 R(s_i)=s_{k-1}.
\tag{1.6c}
\]

Apply the second identity at (i+m): it gives
(R(s_{i+m})=s_{k-m-1}).  Comparing with the first and using
((k+m)-(k-m-1)=2m+1=n) again proves (1.6a).

Thus (X_{i+n}=X_i).  Since the (L) middle windows on the component
are distinct, (n\equiv0\pmod L), so (L\mid n).  A proper divisor of
the odd number (n=2m+1) is at most (n/3<m), and a cyclic word of that
period cannot have an injective (m)-window.  Therefore (L=n).
Corollary 1.2 says every (n-1) cyclic window is injective; on a period of
length (n), this forces all (n) symbols to be distinct.  Its middle
windows are precisely the rotations of one cyclic coordinate order, i.e.
one wreath. \(\square\)

The same conclusion holds when \(\theta\) pairs two distinct components.
Write their symbol words as (s) and (t).  Equations (1.6b) or (1.6c)
then have (t) on their right sides; comparing the equation at (i) with
the shifted equation at (i+m) gives (t_{j+n}=t_j).  Hence the image
component has length (n), and applying the same argument back to its
mate gives length (n) there as well.

### Corollary 1.3a (anti-dihedral component toll)

Any anti-dihedral singleton factor enumerating all (W) middle owners has
exactly (W/n) components.  Linearizing cyclic windows of length (m+H+1)
component by component therefore has excess

\[
 \frac Wn(m+H)
 =\left(\frac12+o(1)\right)W
\]

when (H=o(m)).  Hence the anti-dihedral singleton architecture cannot
produce a (W+o(W)) word by the sliding-spine compiler.  A non-singleton
or nonlocal seam fusion could still reuse positions, but its final
chronology would no longer be the anti-dihedral singleton factor covered
by Theorem 1.3.

### Corollary 1.3b (near-wreath recurrence ledger)

Assume a (not necessarily symmetric) sliding middle Ucycle has one
component and recurrence gap at least (n-1).  Every coordinate occurs in
the symbol word exactly

\[
 B=\frac Wn=\operatorname {Cat}_m
\tag{1.7}
\]

times.  Enumerate the cyclic recurrence gaps of one coordinate as
(g_1,\ldots,g_B).  Then

\[
 \boxed{g_j\ge n-1\quad\text{and}\quad
        \sum_{j=1}^{B}(g_j-(n-1))=B.}
\tag{1.8}
\]

#### Proof

A fixed coordinate belongs to
\(\binom{n-1}{m-1}=mW/n=mB\) middle windows.  One occurrence of a symbol
belongs to exactly (m) middle windows, since every (m)-window is
injective.  Hence its symbol frequency is (B).  The recurrence hypothesis
gives (g_j\ge2m=n-1).  The cyclic gaps sum to the word period
(W=nB), which gives (1.8). \(\square\)

Thus a surviving direct Hamilton spine is not an arbitrary long Ucycle.  It is a
near-wreath rotor: every physical recurrence differs from the shortest
allowable value (n-1) by total excess exactly one per occurrence on
average.  This is a concrete statewise diagnostic for any proposed
reflection half-path.

### Theorem 1.4 (exact two-rotor normal form)

Let (s) be any cyclic word on ([n]) in which every (n-1) consecutive
symbols are distinct.  Put

\[
 P_i=(s_i,s_{i+1},\ldots,s_{i+n-2})
\]

and let (u_i) be the unique coordinate missing from (P_i).  Then

\[
 \boxed{s_{i+n-1}\in\{s_i,u_i\}.}
\tag{1.9}
\]

For the permutation state

\[
 \pi_i=(s_i,s_{i+1},\ldots,s_{i+n-2},u_i)\in S_n,
\tag{1.10}
\]

the two possibilities in (1.9) are exactly

\[
 \begin{array}{c|c|c}
 s_{i+n-1}&u_{i+1}&\pi_i\longmapsto\pi_{i+1}\\ \hline
 s_i&u_i&\text{left rotation of the first }n-1\text{ entries},\\
 u_i&s_i&\text{left rotation of all }n\text{ entries}.
 \end{array}
\tag{1.11}
\]

Conversely, either transition in (1.11) preserves the property that the
first (n-1) entries are distinct and that the last entry is their unique
missing coordinate.

#### Proof

The (n-2) symbols
(s_{i+1},\ldots,s_{i+n-2}) already occupy all but two coordinates of
([n]).  Those two coordinates are (s_i) and (u_i).  The next
((n-1))-window must be injective, so its new last symbol must be one of
these two, proving (1.9).

If it is (s_i), the missing coordinate remains (u_i) and (1.10) is
left-rotated on its first (n-1) positions.  If it is (u_i), the new
missing coordinate is (s_i) and the entire (n)-tuple is left-rotated.
The converse is immediate from the displayed states. \(\square\)

Combining Corollary 1.2 and Theorem 1.4 gives the finite-state formulation
of the **now-closed anti-dihedral candidate**:

> Find a cyclic orbit of length (W) in the two-generator rotor
> automaton on (S_n), generated by the rotations of the first (n-1)
> coordinates and of all (n) coordinates, such that its emitted
> (m)-prefix sets enumerate the middle layer, its shorter prefixes cover
> the lower band, and its induced Middle-Levels cycle is anti-dihedral.

The transition alphabet is only binary, and anti-dihedral symmetry would
make all upper traces automatic.  Theorem 1.3 nevertheless rules out the
required long-component conclusion.  The surviving formulation keeps the
same binary automaton but removes the last clause and imposes both the
lower and upper prefix systems explicitly, as in (1.19)--(1.20).

### Corollary 1.5 (Johnson projection and prefix universality)

Write a state as

\[
 \pi_i=(x_1,\ldots,x_n).
\]

Both rotor moves in (1.11) induce the same next middle owner:

\[
 \boxed{
 X_i=\{x_1,\ldots,x_m\},\qquad
 X_{i+1}=X_i-\{x_1\}+\{x_{m+1}\}.}
\tag{1.12}
\]

The two resulting permutation states agree in their first (n-2)
positions and differ only by transposing their final two entries.  Thus
the binary control is a **tail switch**; it changes future chronology but
not the current Johnson edge.

Moreover,

\[
 S_{i,q}=\{x_1,\ldots,x_{m-q}\},
 \qquad
 Y_i=\{x_1,\ldots,x_{m+1}\}.
\tag{1.13}
\]

Hence the lower condition (0.5) says exactly that the orbit is
simultaneously prefix-universal at the prefix lengths
(m,m-1,\ldots,m-H).  In the closed symmetric candidate, anti-dihedral
duality identifies these with the corresponding upper traces.  In the
surviving non-symmetric candidate, the upper prefixes must instead be
covered directly.

#### Proof

Both transitions delete (x_1) from the first (m) positions and shift
(x_{m+1}) into position (m), proving (1.12).  Inspection of (1.11)
gives the tail transposition.  Equation (1.13) is immediate from the
definition (1.10). \(\square\)

This separates the surviving construction into two exact layers: choose a
Hamilton middle-prefix projection, then choose binary tail switches whose
lift is simultaneously universal for both prefix systems.  No random
per-depth choice is involved.

### Proposition 1.6 (state connectivity and exact fibre bundles)

Let (A) be left rotation of the first (n-1) positions and (B) left
rotation of all (n) positions.  The directed two-rotor state graph on
(S_n), with arcs \(\pi\to A\pi,B\pi\), is strongly connected.

Let

\[
 \mathcal F_X=\{\pi\in S_n:\{\pi_1,\ldots,\pi_m\}=X\}
\]

be the state fibre over a middle owner.  For every Johnson neighbour
(X'=X-\{x\}+\{y\}), exactly

\[
 \boxed{(m-1)!\,m!}
\tag{1.14}
\]

states in \(\mathcal F_X\) project under either rotor move to the edge
(X\to X').

#### Proof

The two outputs (A\pi) and (B\pi) agree in their first (n-2)
positions and differ by the transposition of the last two.  Therefore

\[
 BA^{-1}=(n-1\  n)
\]

as a permutation of positions (up to the harmless left/right action
convention).  Conjugating this transposition by powers of the
((n-1))-cycle (A) gives all star transpositions ((j\ n)), which
generate (S_n).  A finite semigroup generated by permutations is the
group they generate, proving strong connectivity.

For the count, a state over (X) projects to the displayed Johnson edge
exactly when \(\pi_1=x\) and \(\pi_{m+1}=y\).  The remaining (m-1)
members of (X) may be ordered freely in positions (2,\ldots,m), and
the remaining (m) complementary coordinates freely in positions
(m+2,\ldots,n).  This gives (1.14). \(\square\)

Thus there is no state-graph connectivity or local degree obstruction.
The open object is a global fibre transversal: choose one state over every
middle owner so that the chosen states close under one of the two outgoing
rotor arcs, form (o(W/m)) cycles, satisfy the prefix-cover conditions,
and have **no** anti-dihedral requirement.  Proposition 1.6 supplies factorial local freedom
but does not round those simultaneous conditions.

### Theorem 1.7 (exact all-depth fractional rotor circulation)

Put

\[
 D=|\mathcal F_X|=m!(m+1)!.
\tag{1.15}
\]

Fix any \(t\in[0,1]\).  Give the (A)-arc out of every state weight
\(t/D\) and its (B)-arc weight \((1-t)/D\).  Then:

1. the total outgoing root mass over every owner fibre \(\mathcal F_X\)
   is exactly one;
2. inflow equals outflow at every permutation state; and
3. simultaneously for every \(1\le r\le n-1\) and every
   \(S\in\binom{[n]}r\), the total root mass of states whose first
   (r) entries have underlying set (S) is

   \[
   \boxed{\frac W{\binom n r}.}
   \tag{1.16}
   \]

#### Proof

There are (m!) orders of the first (m) coordinates and ((m+1)!)
orders of the rest, proving (1.15).  Each state has total outgoing weight
(1/D), so summing over one fibre gives one.  The two incoming arcs are
the unique (A^{-1})- and (B^{-1})-preimages and have total weight
\(t/D+(1-t)/D=1/D\), proving flow conservation.

For fixed \(S\in\binom{[n]}r\), the number of permutations whose first
(r) entries have set (S) is

\[
 r!(n-r)!.
\]

Multiplying by (1/D) gives

\[
 \frac{r!(n-r)!}{m!(m+1)!}
 =\frac{\binom n m}{\binom n r},
\]

which is (1.16). \(\square\)

The same fractional circulation fixes all prefix depths with one common
state variable; no independent per-depth randomization is being used.
The unresolved theorem is therefore an integral, owner-transversal,
few-cycle rounding of this particular two-generator circulation, satisfying
both prefix-cover systems.  Ordinary flow integrality does not include
the one-state-per-owner-fibre constraints.

At (t=0), the circulation is supported entirely on the full-rotation
(B)-orbits.  Each orbit is one cyclic coordinate order, hence one
wreath, and satisfies plain-complement rotational anti-dihedral symmetry
componentwise.  Thus even shortest-wreath ownership and anti-dihedral
closure occur at one endpoint of the exact fractional segment.  Moreover,
the known exact wreath factorization supplies an integral point in this
same (B)-orbit face, but with exactly (W/n) components.  It is not a
viable symmetry condition for the desired rounding.  The missing content
is the correlated integral choice which simultaneously reduces the
component count and covers both prefix systems after symmetry has been
abandoned.

### Theorem 1.8 (integral circulation equivalence)

For \(g\in\{A,B\}\), let (z_{\pi,g}\in\{0,1\}).  The equations

\[
 \sum_{\pi\in\mathcal F_X}\sum_g z_{\pi,g}=1
 \qquad\left(X\in\binom{[n]}m\right)
\tag{1.17}
\]

and

\[
 \sum_g z_{\pi,g}
 =\sum_g z_{g^{-1}\pi,g}
 \qquad(\pi\in S_n)
\tag{1.18}
\]

are equivalent to a cyclic singleton subset-Ucycle factor whose middle
windows enumerate \(\binom{[n]}m\) exactly once and whose symbol
recurrence gap is at least (n-1).

For such a solution, lower coverage through depth (H) is exactly the
family of inequalities

\[
 \boxed{
 \sum_{\substack{\pi:\{\pi_1,\ldots,\pi_{m-q}\}=S}}
       \sum_gz_{\pi,g}\ge1
 \quad
 \left(S\in\binom{[n]}{m-q},\ 0\le q\le H\right).}
\tag{1.19}
\]

The number of Ucycle components is the number of directed cycles in the
support of (z).

Without anti-dihedral symmetry, direct upper coverage is exactly the
second family of inequalities

\[
 \boxed{
 \sum_{\substack{\pi:\{\pi_1,\ldots,\pi_{m+1+q}\}=U}}
       \sum_gz_{\pi,g}\ge1
 \quad
 \left(U\in\binom{[n]}{m+1+q},\ 0\le q\le H\right).}
\tag{1.20}
\]

For \(H\le m-1\), the recurrence guarantee makes every prefix in
(1.20) a set of the displayed rank.  Under anti-dihedral closure,
(1.20) follows from (1.19) by Theorem 1.1 and is redundant.

#### Proof

Equation (1.17) selects total outgoing degree one in every owner fibre.
Because the variables are Boolean, at most one rotor arc leaves any
state.  Equation (1.18) gives the same selected indegree.  Hence the
selected states and arcs form disjoint directed cycles.  Exactly one state
over every owner occurs, by (1.17).

Along a selected state cycle, Theorem 1.4 says that successive states are
the consecutive frames of one cyclic symbol word with recurrence gap at
least (n-1).  Corollary 1.5 identifies the middle owner with its
(m)-window.  Thus the owner-fibre condition says precisely that all
middle sets occur once.

Conversely, framing every position of a cyclic singleton Ucycle factor by
(1.10) and marking its actual rotor transition gives a Boolean vector
satisfying (1.17)--(1.18).  Finally (1.13) identifies the left sides of
(1.19)--(1.20) with the numbers of selected prefix occurrences of the
displayed targets. \(\square\)

Thus the two-sided Gaussian endpoint theorem is now a completely explicit
integer-circulation problem with factorially large fibres, two outgoing
arcs per state, uniform fractional point (Theorem 1.7), prefix-cover cuts
(1.19)--(1.20), and a sub-Catalan cycle target.  This is
strictly smaller than quantifying over arbitrary literal words while still
being sufficient for the original coefficient-one endgame.

## 2. The nested-Ucycle literalization theorem

There is an exact local test for when a directed Johnson Hamilton cycle
has the required singleton encoding.  Write

\[
 X_{i+1}=X_i-\{d_i\}+\{a_i\}.
\tag{2.0a}
\]

### Proposition 2.0 (long-cycle residence test)

The cycle has a cyclic symbol encoding

\[
 X_i=\{s_i,s_{i+1},\ldots,s_{i+m-1}\}
\quad(i\in\mathbb Z_W)
\tag{2.0b}
\]

if and only if

\[
 \boxed{a_i=d_{i+m}\quad\text{for every }i}
\tag{2.0c}
\]

and every (m+1) consecutive terms of the cyclic deletion word
(d=(d_i)) are distinct.  In that case one may take (s_i=d_i).

#### Proof

If (2.0b) holds, the transition from (X_i) to (X_{i+1}) deletes
(s_i) and adds (s_{i+m}), proving (2.0c).  Every (m)-window is a
set.  Also (s_{i+m}\ne s_i), since equality would give
(X_{i+1}=X_i); hence every (m+1) consecutive symbols are distinct.

Conversely, put

\[
 D_i=\{d_i,d_{i+1},\ldots,d_{i+m-1}\}.
\]

The distinctness hypothesis makes this an (m)-set and gives

\[
 D_{i+1}=D_i-\{d_i\}+\{d_{i+m}\}
          =D_i-\{d_i\}+\{a_i\}.
\tag{2.0d}
\]

It remains only to identify one state.  For (0\le j<m), the element
(d_j) is present in (X_j) and was not among the additions
(a_0=d_m,\ldots,a_{j-1}=d_{m+j-1}), because each such equality would
repeat a deletion label at cyclic distance at most (m).  Reading the
first (j) transitions backwards therefore gives (d_j\in X_0).
Thus (D_0\subseteq X_0); both have size (m), so (D_0=X_0).
Equation (2.0d) and the Johnson recurrence now give (D_i=X_i) for all
(i).  Taking (s_i=d_i) proves (2.0b). \(\square\)

Assume (0.1)--(0.2), with the (X_i)'s enumerating the middle layer.
Every (m)-term window is a set.  Moreover every (m+1)-term window is a
set: if (s_{i+m}) repeated one of
(s_{i+1},\ldots,s_{i+m-1}), then (X_{i+1}) would have fewer than (m)
elements; if (s_{i+m}=s_i), then (X_{i+1}=X_i), contradicting the
bijection in (0.2).  Hence

\[
 Y_i=X_i\cup X_{i+1}
     =\{s_i,s_{i+1},\ldots,s_{i+m}\}
\tag{2.1}
\]

has rank (m+1).

For (q\le m-1), direct overlap of sliding windows gives

\[
 \bigcap_{j=0}^{q}X_{i-j}
 =\{s_i,s_{i+1},\ldots,s_{i+m-q-1}\}
 =S_{i,q}.
\tag{2.2}
\]

Indeed every (m+1) consecutive symbols are distinct, so two occurrences
of one symbol have cyclic separation at least (m+1).  One occurrence at
position (t) belongs exactly to the (m)-windows whose starts lie in
\([t-m+1,t]\).  Two such start intervals coming from consecutive
occurrences have at least one uncovered start between them.  Hence a
symbol lying in all \((q+1)\) windows in (2.2) must have one occurrence in
their common positional overlap.  The reverse inclusion is immediate.

The upper traces are literal long windows:

\[
 U_{i,q}=\bigcup_{j=0}^{q+1}X_{i+j}
 =\{s_i,s_{i+1},\ldots,s_{i+m+q}\}.
\tag{2.3}
\]

The equality in (2.3) is equality of sets, so repeated symbols, if any,
cause no problem.  Under (0.4) and Theorem 1.1, however, every such trace
which is dual to a lower trace has rank exactly (m+1+q).

### Theorem 2.1 (one-sided nested Ucycle implies a two-sided word)

Assume (0.1)--(0.5), where (0\le H<m).  Form the linear word of
singleton masks

\[
 Z=(\{s_0\},\ldots,\{s_{W-1}\},
       \{s_0\},\ldots,\{s_{m+H-1}\}).
\tag{2.4}
\]

Then (Z) has length (W+m+H) and represents every set in the paired
central band (0.7).

More precisely:

1. (X_i) is represented by the length-(m) interval beginning at (i);
2. (S_{i,q}) is represented by the length-((m-q)) interval beginning
   at (i), and shares its left endpoint with (X_i);
3. every upper trace of depth (q) is a length-((m+1+q)) interval; and
4. an upper trace beginning at (a) shares its right endpoint with the
   rank-((m+1)) suffix window beginning at (a+q).

#### Proof

Appending the first (m+H) symbols linearizes every cyclic interval of
length at most (m+H+1).  Assertions 1--2 follow from (0.2), (0.5), and
(2.2).

By hypothesis the lower traces at depth (q) cover all of
\(\binom{[n]}{m-q}\).  Theorem 1.1 maps their multiset bijectively to
upper traces and maps the target layer bijectively onto
\(\binom{[n]}{m+1+q}\).  Thus the upper traces cover that entire layer.
Equation (2.3) makes every such trace a literal interval of (2.4).

Finally the length-((m+1+q)) interval
\([a,a+m+q]\) has the length-((m+1)) suffix
\([a+q,a+m+q]\).  They share the right endpoint, proving assertion 4.
All statements remain valid for intervals crossing the cyclic cut because
of the appended prefix.  \(\square\)

### Corollary 2.2 (formal sharpness, and why the shortcut fails)

In Theorem 2.1 all (W) rank-(m) witnesses have length (m), and all
(W) rank-((m+1)) witnesses have length (m+1).  At every depth the
lower flags can be chosen with common left endpoints and the upper flags
with common right endpoints.

Thus, formally, Theorems 3.1 and 3.3 of the long-endpoint obstruction are
met with density one and span \(\Theta(m)\).  But Theorem 1.3 says that a
component satisfying the anti-dihedral hypothesis has length only (n).
For (W>n), the one-component hypothesis of Theorem 2.1 is therefore
impossible.  The theorem records the exact implication which motivated
the route; Theorem 1.3 closes it at the component-count gate.

### Corollary 2.3 (the former endgame is vacuous)

If Theorem 2.1 is available for some

\[
 H=\sqrt m\,\omega(m),
 \qquad \omega(m)\to\infty,
 \qquad H=o(m),
\tag{2.5}
\]

then the central word has length (W+o(W)).  Appending the audited
product-SCD exterior word beyond this band costs (o(W)).  Hence the
constant-one upper bound follows in odd dimension, and the standard
trimmed lift gives the even-dimensional statement.

Theorem 1.3 proves that this hypothesis cannot hold on one component for
large (m).  Thus the implication is logically correct but supplies no
construction.  The surviving endgame is the direct two-sided rotor
compiler below.

### Theorem 2.4 (direct two-sided rotor compiler)

Let (z) be a Boolean rotor circulation satisfying (1.17)--(1.18) and
both prefix-cover systems (1.19)--(1.20) through depth (H\le m-1).
Let (C(z)) be the number of directed cycles in its support.  Then there
is a literal singleton word of length at most

\[
 \boxed{W+C(z)(m+H)}
\tag{2.6}
\]

covering every rank in \([m-H,m+1+H]\).  Every middle owner has a
length-(m) witness and every upper central owner a length-((m+1))
witness.  The lower flags use common left endpoints and the upper flags
use common right endpoints.

In particular,

\[
 H=o(m),\qquad C(z)=o(W/m)
\tag{2.7}
\]

imply a word of length (W+o(W)).

#### Proof

Theorem 1.8 turns every support cycle into a cyclic singleton word with
recurrence gap at least (n-1), and the middle windows across the cycles
enumerate the middle layer exactly.  Conditions (1.19)--(1.20) give the
two required prefix covers.

For each support cycle write one period and repeat its first (m+H)
symbols.  Every protected cyclic prefix is then a literal interval.
Concatenate the resulting (C(z)) blocks.  A lower window of length
(m-q) shares its left endpoint with the length-(m) prefix.  An upper
window of length (m+1+q) shares its right endpoint with its
length-((m+1)) suffix.  This proves (2.6), and (2.7) makes its excess
(o(W)). \(\square\)

### Corollary 2.5 (surviving conditional coefficient-one endgame)

If Theorem 2.4 is available for

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\to\infty,\qquad H=o(m),\qquad C(z)=o(W/m),
\tag{2.8}
\]

then the audited product-SCD exterior word costs (o(W)), and the
constant-one upper bound follows.  Theorem 1.7 satisfies every prefix-rank
margin fractionally.  The missing content is its correlated integral
owner-transversal rounding with both prefix covers and sub-Catalan cycle
count.

### Corollary 2.6 (anti-dihedral redundancy is unusable)

Anti-dihedral closure would make (1.20) follow from (1.19).  Theorem 1.3
(with the same calculation when two components are paired) forces every
such component to have length (n).  Hence (C(z)=W/n\), contradicting
the little-(o) condition in (2.7).  The surviving singleton-spine gate
must impose both prefix systems directly; reflection or rotation cannot
remove the upper half.

There is no symmetry cost at the fractional or initial integral point.
For one wreath with
cyclic order \(\pi\),

\[
 X_i=I_\pi(i,m),\qquad Y_i=I_\pi(i,m+1)
\]

satisfy

\[
 X_i^c=Y_{i+m}.
\tag{2.10}
\]

Hence every exact wreath factor is already a plain-complement rotational
anti-dihedral nested-window factor, but with exactly (W/n) short
components and with possibly defective shadows.  Rotor tail-switches may
fuse or alter these components, but Theorem 1.3 says that every successful
fusion must break anti-dihedral symmetry.  It must then meet both explicit
prefix systems (1.19)--(1.20) directly.

## 3. Reflection symmetry has an exact half-path normal form

Plain complement cannot act as a reflection of a Middle-Levels Hamilton
cycle: it fixes neither a vertex nor an edge.  A reverse-complement
involution has a different geometry and has exponentially many possible
axis edges.

Let (R) be an involution of ([n]) with one fixed point (z) and (m)
two-element orbits, and put

\[
 \theta(A)=[n]\setminus R(A).
\tag{3.1}
\]

### Lemma 3.1 (fixed-edge census)

A Middle-Levels edge is fixed setwise by (\theta) if and only if it is

\[
 \boxed{\{A,A\cup\{z\}\},}
\tag{3.2}
\]

where (A) chooses exactly one point from each two-element orbit of
(R).  Hence (\theta) has exactly (2^m) fixed Middle-Levels edges.

#### Proof

If (A) chooses one point from each pair and avoids (z), then
(R(A)) consists of the opposite choices, so

\[
 [n]\setminus R(A)=A\cup\{z\},
 \qquad
 [n]\setminus R(A\cup\{z\})=A.
\]

Thus (3.2) is fixed setwise.

Conversely, a fixed edge has the form \(\{A,\theta(A)\}\) with
\(|A|=m\) and (A\subset\theta(A)).  The inclusion is equivalent to
(A\cap R(A)=\varnothing).  Therefore (A) avoids (z) and contains at
most one point from each of the (m) two-element orbits.  Since
\(|A|=m\), it contains exactly one from each.  This proves the
classification and count.  \(\square\)

### Theorem 3.2 (reflection half-path equivalence)

A (\theta)-reflection-invariant Hamilton cycle of the Middle Levels
graph is equivalent to a path

\[
 P=(v_0,v_1,\ldots,v_{W-1})
\tag{3.3}
\]

which:

1. contains exactly one vertex from every two-element (\theta)-orbit;
2. has \(\{v_0,\theta(v_0)\}\) and
   \(\{v_{W-1},\theta(v_{W-1})\}\) as Middle-Levels edges.

Given (P), the Hamilton cycle is

\[
 v_0,v_1,\ldots,v_{W-1},
 \theta(v_{W-1}),\theta(v_{W-2}),\ldots,\theta(v_0),v_0.
\tag{3.4}
\]

#### Proof

Conditions 1--2 make (3.4) a cycle: the two joining edges are the two
displayed fixed-axis edges, and the second half is the (\theta)-image
of the first half in reverse order.  It visits both members of every
orbit, hence every Middle-Levels vertex exactly once.  Reflection across
the two joining edges is precisely (\theta).

Conversely, cut a (\theta)-reflection-invariant Hamilton cycle at its
two fixed edges.  Either open half is a path of the form (3.3), and the
reflection pairs its vertices bijectively with those on the other half.
Thus it contains one representative from every orbit and has the stated
endpoint property.  \(\square\)

Theorem 3.2 is a genuine simplification of the reflection search: the
Hamilton condition lives on (W), rather than (2W), vertices, and the
axis choices come from the explicit (2^m)-edge family in Lemma 3.1.
It does **not** supply the sliding-window residence law or the lower
all-depth coverage.  More decisively, Theorem 1.3 proves that no such
reflection Hamilton cycle can also be one long singleton sliding-window
component.  The half-path normal form remains relevant only for a
non-singleton or otherwise nonlocal literalization.

## 4. The SCD endpoint skeleton inside the new gate

An SCD gives an exact lower flag ending at every rank-(m) owner.  It can
be used as a certificate for (0.5) if it embeds into the sliding windows.

### Definition 4.1 (window-compatible lower SCD skeleton)

For each SCD chain (C), let (X(C)) be its rank-(m) member and let
(r(C)) be its depth below rank (m).  A cyclic word (0.1) is compatible
with the lower half of the SCD if there is a bijection (C\mapsto i(C))
such that

\[
 X(C)=X_{i(C)},
 \qquad
 \text{the unique member of }C\cap\binom{[n]}{m-q}
   \text{ is }S_{i(C),q}
 \quad(0\le q\le r(C)).
\tag{4.1}
\]

### Proposition 4.2 (SCD compatibility discharges lower coverage)

If (4.1) holds through depth (H), then (0.5) covers every lower layer
through depth (H), indeed with a distinguished occurrence of every
target and with no distinguished collisions.

#### Proof

The SCD partitions the Boolean lattice.  Every target of rank (m-q)
lies on its unique SCD chain, which necessarily has depth at least (q).
Equation (4.1) identifies that target with the corresponding window
(S_{i(C),q}).  Distinct targets have distinct SCD occurrences. \(\square\)

Thus the formerly proposed reflection-symmetric SCD target was:

> Find the half-path of Theorem 3.2 whose rank-(m) projection admits a
> cyclic singleton encoding compatible with the lower half of one SCD.

Theorem 1.3 now closes this target negatively: a reflection-compatible
singleton component has length (n), not (W).  Static SCD ownership and
reflection symmetry may still inform a non-singleton braid, but they
cannot be combined through one sliding singleton spine.  For the surviving
binary-rotor route, an SCD embedding could discharge (1.19), while (1.20)
must be handled independently.

## 5. Exact remaining boundary

Proved here:

1. anti-dihedral symmetry identifies the full lower and upper trace
   multisets at every depth;
2. that same symmetry forces (s_{i+n}=s_i), so every compatible
   singleton component is exactly one wreath and the anti-dihedral
   component-compression route is closed;
3. every recurrence-((n-1)) singleton spine has the exact binary
   two-rotor normal form, with factorial Johnson edge bundles;
4. the rotor graph has an exact common all-rank fractional circulation;
5. Boolean fibre-transversal circulations are exactly singleton Ucycle
   factors, with lower and upper coverage given by (1.19)--(1.20);
6. such a circulation with (o(W/m)) cycles has a direct literalization
   of length (W+o(W)), meeting the Gaussian long-endpoint requirement at
   density one; and
7. reverse-complement reflections reduce to a transversal Hamilton path
   between two explicitly classified fixed edges, though that path cannot
   also be one long singleton component.

Not proved here:

1. an integral solution of (1.17)--(1.20) with (o(W/m)) support cycles
   in a growing Gaussian window;
2. a non-singleton reflection/SCD braid which evades Theorem 1.3; or
3. the constant-one theorem.

The reflection experiment therefore has a definitive verdict: it closes
the upper ledger but is too rigid to permit long singleton components.
The surviving endpoint-skeleton route is the **direct two-sided binary
rotor circulation**.  Its fractional geometry and literal compiler are
complete; its correlated integral prefix-cover rounding and component
count are the exact remaining theorem.
