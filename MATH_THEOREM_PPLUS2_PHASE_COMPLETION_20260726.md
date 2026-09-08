# Exact phase completion on a near-minimal \(p+2\) component

Date: 2026-07-26

Method: pure mathematics only.

## 1. Setup

Let \(p=2m+1\) be an odd prime.  Consider a singleton-signature
row--necklace component having \(p+2\) row vertices and \(p+2\) necklace
columns.  Index its incidence matrix by columns and rows:

\[
 B_{ji}=1\quad\Longleftrightarrow\quad
 \text{row \(i\) has one occurrence in necklace column \(j\)}.
\]

Every row and column sum is \(p\).  The bipartite complement is
2-regular.  Choose one of its two perfect matchings as the identity.  The
other is a permutation matrix \(P\), so

\[
 \boxed{B=J-(I+P).}
\tag{1.1}
\]

The two complementary matchings are edge-disjoint.  Hence \(P\) has no
fixed point.  For each column \(j\), let \(M_j\) be its two missing rows
and

\[
 N_j=[p+2]\setminus M_j
\]

its \(p\) incident rows.  The two rows in \(M_j\) are consecutive on one
cycle of \(P\).

For every incidence \(i\in N_j\), let

\[
 \phi_{ij}\in\mathbb F_p
\]

be its original physical phase in column \(j\).  Exact middle ownership
means that, for every column,

\[
 \phi_j:N_j\longrightarrow\mathbb F_p,qquad
 i\longmapsto\phi_{ij},
\tag{1.2}
\]

is a bijection.

An ordinary one-shift-per-row lift chooses \(a_i\in\mathbb F_p\) and
replaces every incident phase \(\phi_{ij}\) by \(\phi_{ij}+a_i\).  It is
legal exactly when every shifted column is again a complete residue
system.

---

## 2. First moments

The first power sum at every column gives

\[
 Ba=0\quad\text{over }\mathbb F_p.
\tag{2.1}
\]

The complement-kernel calculation gives

\[
 \boxed{
 \ker_{mathbb F_p}B
 =\langle\mathbf1\rangle
  \oplus\bigoplus_{C\in\mathcal C_{\rm even}(P)}
       \langle\varepsilon_C\rangle,}
\tag{2.2}
\]

where \(\varepsilon_C\) is supported on an even cycle \(C\) of \(P\)
and alternates \(+1,-1,+1,-1,\ldots\) around it.  Thus every
first-moment solution has the form

\[
 a=c\mathbf1+sum_{C\ {m even}}t_C\varepsilon_C.
\tag{2.3}
\]

The common shift \(c\) is harmless: translating all \(p\) phases of a
column by \(c\) preserves the complete residue system.  The question is
whether any nonzero alternating part survives all higher moments.

---

## 3. All power sums are one permutation condition

Remove the common shift and write \(d_i=a_i-c\).  At column \(j\), use
the original phase bijection to define

\[
 T_j(x)=x+d_{\phi_j^{-1}(x)}
 \qquad(x\in\mathbb F_p).
\tag{3.1}
\]

### Theorem 3.1 -- exact column completion criterion

The row-shift assignment \(a\) is legal if and only if

\[
 \boxed{T_j\in\operatorname{Sym}(\mathbb F_p)
 \quad\text{for every column }j.}
\tag{3.2}

Equivalently, for every \(j\) and every \(0\le k\le p-1\),

\[
 \boxed{
 \sum_{i\in N_j}
 \left[(\phi_{ij}+d_i)^k-\phi_{ij}^k\right]=0.}
\tag{3.3}
\]

If the column phase labels are not fixed in advance, let

\[
 D_j=\{d_i:i\in N_j\}
\]

be the displacement multiset.  There exists some phase bijection \(\phi_j\)
making column \(j\) legal if and only if \(D_j\) is the displacement
multiset of a permutation of \(\mathbb F_p\):

\[
 \boxed{
 D_j=\{\tau(x)-x:x\in\mathbb F_p\}
 \quad\text{as multisets for some }\tau\in S_p.}
\tag{3.4}
\]

#### Proof

The shifted column contains the phases \(T_j(x)\), one for every
\(x\in\mathbb F_p\).  They are a complete residue system exactly when
\(T_j\) is a permutation, proving (3.2).

Equality of the old and new multisets is equivalent to equality of sums
against every function on \(\mathbb F_p\).  The monomials
\(1,x,\ldots,x^{p-1}\) span all such functions, proving (3.3).

If \(\phi_j\) is legal, take \(\tau=T_j\); its displacement at the old
phase \(x=\phi_{ij}\) is \(d_i\), proving necessity in (3.4).
Conversely, match the rows having each displacement value to the phase
positions having that displacement under \(\tau\).  This defines a phase
bijection for which (3.1) is \(\tau\). \(\square\)

This is the complete higher-moment classification for an arbitrary fixed
column phase array.  The remaining sections make it explicit for one
alternating cycle.

---

## 4. Permutations with displacements \(0,\pm t\)

### Lemma 4.1 -- transposition classification

Let \(t\ne0\) in \(\mathbb F_p\).  Suppose a permutation \(\tau\) has
displacement multiset

\[
 \{\tau(x)-x:x\in\mathbb F_p\}
 =\{(+t)^r,(-t)^r,0^{p-2r}\}.
\tag{4.1}
\]

Then \(\tau\) is the product of \(r\) disjoint transpositions

\[
 x_\ell\longleftrightarrow x_\ell+t
 \qquad(1\le\ell\le r)
\tag{4.2}
\]

and fixes every remaining phase.  Conversely every such product has
displacement multiset (4.1).  Such a permutation exists exactly when

\[
 0\le r\le m=\frac{p-1}{2}.
\tag{4.3}
\]

#### Proof

Scale phases so that \(t=1\).  Every nonfixed arrow
\(x\mapsto\tau(x)\) is an edge of the undirected cycle \(C_p\).  A cycle
of the permutation having length at least three would be a simple cycle
in \(C_p\), hence would use all \(p\) vertices.  The only two directed
Hamilton cycles of \(C_p\) have all displacements \(+1\) or all
displacements \(-1\), incompatible with the equal numbers in (4.1).
Thus every nontrivial permutation cycle has length two and is an adjacent
transposition.  This proves (4.2).  Conversely such transpositions plainly
work.  Their edges form a matching in \(C_p\), whose maximum size is
\((p-1)/2\). \(\square\)

---

## 5. One even complement cycle: necessary and sufficient pairing

Fix an even cycle \(C\) of \(P\), of length \(2h\), and orient its
alternating vector as

\[
 C=C^+\sqcup C^-,\qquad
 \varepsilon_C=+1\text{ on }C^+,quad
 \varepsilon_C=-1\text{ on }C^-.
\]

Consider the nonconstant first-moment direction

\[
 a=t\varepsilon_C,qquad t\ne0,
\tag{5.1}
\]

with zero shift off \(C\).  At column \(j\), put

\[
 X_j^+=\{\phi_{ij}:i\in C^+\cap N_j\},\qquad
 X_j^-=\{\phi_{ij}:i\in C^-\cap N_j\}.
\tag{5.2}
\]

The two sets have the same size

\[
 r_j=
 \begin{cases}
 h-1,&j\text{ lies on the same complement cycle }C,\\
 h,&j\text{ lies on another complement cycle.}
 \end{cases}
\tag{5.3}
\]

Indeed, a column on \(C\) omits two consecutive cycle rows, one of each
sign; a column off \(C\) omits no row of \(C\).

### Theorem 5.1 -- exact alternating completion theorem

The nonconstant assignment (5.1) is legal on the fixed phase array if and
only if, for every column,

\[
 \boxed{X_j^-=X_j^++t.}
\tag{5.4}
\]

Equivalently, at every column the affected phase positions split into
disjoint swaps

\[
 x\longleftrightarrow x+t,
\tag{5.5}
\]

with the \(+\) row at \(x\) and the \(-\) row at \(x+t\).

#### Proof

At column \(j\), the displacement is \(+t\) on \(X_j^+\), \(-t\) on
\(X_j^-\), and zero elsewhere.  The two nonzero displacement counts are
both \(r_j\).  Theorem 3.1 and Lemma 4.1 say that the induced map is a
permutation exactly when every nonfixed point belongs to a transposition
\(x\leftrightarrow x+t\).  This is precisely (5.4). \(\square\)

### Power-sum form

For every column, the complete hierarchy is

\[
 \sum_{x\in X_j^+}\bigl[(x+t)^k-x^k\bigr]
 +\sum_{y\in X_j^-}\bigl[(y-t)^k-y^k\bigr]=0
 \quad(1\le k\le p-1).
\tag{5.6}
\]

The second moment alone is

\[
 \boxed{
 2\left(\sum_{x\in X_j^+}x-
          \sum_{y\in X_j^-}y\right)
 +2r_jt=0.}
\tag{5.7}
\]

It is necessary but not generally sufficient.  All higher equations
together are equivalent to (5.4): when \(y=x+t\), the two summands in
(5.6) cancel pairwise for every function, and conversely Theorem 3.1 plus
Lemma 4.1 forces exactly those pairs.

Thus higher moments do not universally kill the first alternating
direction.  They convert it into an exact phase-pairing condition.

### Corollary 5.2 -- several cycles with one amplitude

Let \(\mathcal A\) be any family of even cycles of \(P\), orient an
alternating sign on each, and put

\[
 a=t\sum_{C\in\mathcal A}\varepsilon_C
 \qquad(t\ne0).
\tag{5.8}
\]

At every column, the incident nonzero shifts again consist of equally many
\(+t\)'s and \(-t\)'s.  If \(X_j^+\) and \(X_j^-\) now denote the unions
of the corresponding phase sets over all active cycles, then (5.8) is
legal if and only if

\[
 \boxed{X_j^-=X_j^++t\quad\text{for every }j.}
\tag{5.9}
\]

The number of each sign is at most \(m\), because the total number of
incident nonzero rows is even and at most the odd number \(p\).  Hence the
abstract columnwise construction of Section 6 works unchanged.

If different even cycles use different amplitudes \(t_C\), longer cycles
of the phase permutation may mix those displacement lengths.  The exact
classification is then Theorem 3.1; it need not reduce to independent
transpositions.

---

## 6. Abstract Latin phase arrays do realize the direction

The pairing condition is not contradictory at the incidence/Latin level.

### Theorem 6.1 -- abstract completion exists

For every even cycle \(C\), every \(t\ne0\), and every incidence matrix
\(B=J-(I+P)\) as above, there is a singleton phase array
\((\phi_{ij})\) such that

1. every original column is a complete residue system;
2. the nonconstant shift \(a=t\varepsilon_C\) is legal.

#### Proof

Because \(P\) has no fixed point, an even cycle cannot have length
\(p+1\): the remaining one vertex would be a fixed point.  Hence
\(h\le m\).  Therefore every \(r_j\) in (5.3) is at most \(m\).

For each column independently, choose \(r_j\) disjoint edges

\[
 x_\ell\longleftrightarrow x_\ell+t
\]

in the phase cycle generated by \(t\).  Assign the incident \(+\) rows
bijectively to the \(x_\ell\)'s and the incident \(-\) rows to the
\(x_\ell+t\)'s.  Assign all unchanged incident rows bijectively to the
remaining phases.  This makes the original column a permutation and
satisfies (5.4).  Columns may be labeled independently in the abstract
singleton incidence model. \(\square\)

Consequently no theorem using only

* the \(p\)-regular incidence matrix,
* singleton signatures, and
* columnwise Latin/all-different constraints

can rule out the alternating direction.  Any exclusion must use geometry
linking the phase labels of different columns.

---

## 7. The first genuinely wreath-specific condition

Let \(\widehat X_j\) be a fixed representative of middle necklace \(j\),
and let \(\sigma\) be the coordinate \(p\)-cycle.  The physical middle set
on incidence \((i,j)\) is

\[
 \sigma^{\phi_{ij}}\widehat X_j.
\tag{7.1}
\]

For an abstract column-Latin array to arise from actual wreath rows, every
row \(i\) must satisfy a cross-column odd-graph condition: its \(p\)
physical middle sets must admit a cyclic ordering
\(j_{i,0},\ldots,j_{i,p-1}\) such that

\[
 \boxed{
 \sigma^{\phi_{i,j_{i,k}}}\widehat X_{j_{i,k}}
 \cap
 \sigma^{\phi_{i,j_{i,k+1}}}\widehat X_{j_{i,k+1}}
 =\varnothing
 \quad(k\in\mathbb Z_p).}
\tag{7.2}
\]

Equivalently, the selected sets in each row must form a shortest
\(p\)-cycle in the odd graph; such a cycle is exactly a wreath.

Condition (7.2) is the first genuinely wreath-specific gate.  It couples
phase labels across different columns and is completely absent from the
independent construction in Theorem 6.1.  Once a row is a wreath, shifting
all its phases by \(a_i\) preserves that row automatically; only column
ownership remains to be checked.  Therefore the unresolved geometric
question is precisely whether a wreath-realizable phase array can satisfy
the simultaneous transposition pairing (5.4) in every column.

This note proves neither a universal wreath realization nor a universal
wreath no-go.  It proves that the incidence and higher column moments alone
cannot decide the question.

### Theorem 7.1 -- inertness and coherent row pairing

For a legal single-amplitude assignment \(a=t\varepsilon_C\), let the
columnwise transposition pairing from (5.4) match every incident \(+\) row
to an incident \(-\) row.  The resulting lift merely permutes the old
wreath rows if and only if these columnwise pairings are restrictions of
one fixed bijection

\[
 \pi:C^+\longrightarrow C^-
\tag{7.3}
\]

such that, for every \(i\in C^+\),

\[
 \boxed{
 N(\pi(i))=N(i),\qquad
 \phi_{\pi(i),j}=\phi_{i,j}+t
 \quad(j\in N(i)).}
\tag{7.4}
\]

In that case the physical wreath supports satisfy

\[
 C_{\pi(i)}=\sigma^t C_i,
\tag{7.5}
\]

and the ordinary lift swaps every paired row.

#### Proof

If (7.4) holds, then at every common necklace column the physical member of
row \(\pi(i)\) is

\[
 \sigma^{\phi_{\pi(i),j}}\widehat X_j
 =\sigma^t\sigma^{\phi_{i,j}}\widehat X_j.
\]

The equal necklace neighborhoods show that this identifies the complete
row supports, proving (7.5).  The negative row shifts back by \(-t\), so
the two rows are exchanged.

Conversely, if the lifted row \(\sigma^t C_i\) is one of the old rows,
call it \(C_{\pi(i)}\).  Coordinate translation preserves every necklace,
so the two rows have identical necklace neighborhoods, and equality of
their physical members gives the phase identity in (7.4).  The local
column transposition theorem forces \(\pi(i)\) to have negative sign.
Doing this for every positive row gives the bijection. \(\square\)

### Corollary 7.2 -- a complement 2-cycle is completely inert

Normalize the common component shift \(c\) to zero.  If \(C\) has length
two, write its rows as \(i_+\) and \(i_-\).  The two
cycle columns omit both rows, while all other \(p\) columns contain both.
Condition (5.4) therefore says

\[
 \phi_{i_-,j}=\phi_{i_+,j}+t
 \quad\text{on every incident column }j.
\tag{7.6}
\]

Hence

\[
 C_{i_-}=\sigma^tC_{i_+}.
\tag{7.7}
\]

The ordinary \(\pm t\) lift swaps the two rows and changes neither the
factor nor any lower row packet: the established middle-packet rigidity
lemma recovers every cyclic interval packet from the middle packet.  The
special partial completion (8.4)
selects \(C_{i_+}\) and \(\sigma^tC_{i_+}=C_{i_-}\) in place of the same
two old rows, so it too reproduces the identical family.

Thus a potentially productive **nonconstant internal direction** must live
on a complement cycle of length at least four.  This does not declare the
component-global constant shift inert; that separate phase may still change
the component row family.

### Corollary 7.3 -- longer complement cycles cannot split into fixed pairs

Two distinct rows of \(B=J-(I+P)\) have the same necklace neighborhood if
and only if they form a 2-cycle of \(P\).  Consequently, on one complement
cycle of length at least four, the coherent fixed-pair condition (7.4) is
impossible.  Any legal nonzero alternating lift on such a cycle is a
genuinely new exact factor rather than a permutation of its old rows.  The
same statement holds for the special partial completion (8.4): it
reproduces the old family exactly when its added translate rows are the
omitted rows under one fixed pairing, which is again (7.4).

#### Proof

Two rows have the same incidence neighborhood exactly when they have the
same two missing complement neighbors.  In the 2-regular bipartite
complement, this means those two row vertices and their two column
neighbors form one 4-cycle.  After one complementary matching is contracted,
this is exactly a 2-cycle of \(P\).  Apply Theorem 7.1. \(\square\)

More generally, for any phase assignment, inertness is characterized by a
permutation \(\pi\) of the rows satisfying

\[
 N(\pi(i))=N(i),\qquad
 \phi_{\pi(i),j}=\phi_{i,j}+a_i
 \quad(j\in N(i)).
\tag{7.8}
\]

Thus the column pairing graph is inert exactly when it decomposes into
globally fixed translate classes with identical necklace neighborhoods;
local phase pairings which change partners from column to column do not
give row-family inertness.

### Theorem 7.3A -- every alternating cycle is a relabeling trade

Let one complement cycle have length `2h`, with alternating shores
`C^+` and `C^-`, and suppose the nonzero amplitude `t` satisfies the exact
pairing condition (5.4).  Then

\[
 \boxed{
   \bigsqcup_{R\in C^+}\sigma^tR
   =
   \bigsqcup_{R\in C^-}R,}
 \qquad
 \boxed{
   \bigsqcup_{R\in C^-}\sigma^{-t}R
   =
   \bigsqcup_{R\in C^+}R.}                                  \tag{7.8a}
\]

Consequently the first equality is a union of connected components of the
ordinary ownership overlay between `sigma^t F` and `F`, using exactly `h`
rows on each side.  The second equality is its translated inverse.  Thus
an actual productive `p+2` direction can occur only if `G_(sigma^t)(F)`
has a union of interaction components with total side size at most
`(p+1)/2`.

#### Proof

Fix a necklace column.  Condition (5.4) pairs every incident positive-row
phase `x` with an incident negative-row phase `x+t`.  Hence, in physical
middle sets, the occurrences supplied in that column by the shifted
positive rows are exactly those supplied by the old negative rows.  The
two complement-neighbor omissions remove one row of each sign on a column
of this cycle and remove neither sign on every other column, so the two
multisets have the same size in every case.  Taking their disjoint union
over all necklace columns proves the first equality.  Translate it by
`sigma^(-t)` to obtain the second.

Each side of the first equality is a family of pairwise middle-disjoint
wreaths, and both sides partition the same physical support.  In the
ownership overlay, no edge can leave that support, so it is a union of
connected components.  The row count is `|C^+|=|C^-|=h`.  Finally an
even cycle in `p+2` vertices has length at most `p+1`, because `p` is odd,
so `h<=(p+1)/2`. \(\square\)

This theorem converts the remaining cross-column question into a small-
component question for a familiar exact-factor overlay.  It does not by
itself exclude the direction: a union of several smaller components may
have total side size `h`, and length four is the first case where the
column pattern forces the connected `K_(2,2)` overlay below.

### Theorem 7.4 -- a length-four cycle is two independent degree-two trades

Let the complement cycle have cyclic row order

\[
 A^+,B^-,C^+,D^-.
\]

Assume the pairing condition (5.4).  Then, as disjoint unions of physical
middle packets,

\[
 \boxed{
 \sigma^tA\sqcup\sigma^tC=B\sqcup D,}
\tag{7.9}
\]

and

\[
 \boxed{
 \sigma^{-t}B\sqcup\sigma^{-t}D=A\sqcup C.}
\tag{7.10}
\]

Each equality is a nontrivial two-for-two wreath trade.  Its ownership
overlay has underlying simple graph \(K_{2,2}\).

#### Proof

At each column, (5.4) says that the phases supplied by the shifted positive
rows are exactly the old phases supplied by the negative rows.  Taking the
disjoint union over all columns proves (7.9).  Applying the inverse phase
swap proves (7.10).

There are four complement-cycle columns.  They respectively omit the
adjacent row pairs

\[
 AB,\quad BC,\quad CD,\quad DA.
\]

At those columns the incident affected pairs are, respectively,

\[
 (C,D),\quad(A,D),\quad(A,B),\quad(C,B).
\]

The phase pairing therefore places at least one physical middle owner in
each of the four cells

\[
 (\sigma^tC,D),\quad(\sigma^tA,D),\quad
 (\sigma^tA,B),\quad(\sigma^tC,B)
\]

of the overlay for (7.9).  Its underlying graph is \(K_{2,2}\).  The
inverse statement gives the same conclusion for (7.10).  In particular,
neither equality splits into two translate-row identities, in agreement
with Corollary 7.3. \(\square\)

The ordinary \(\pm t\) lift performs both disjoint trades (7.9) and
(7.10) simultaneously.  The special \(\{0,2\}\) completion (8.4) keeps
\(A,C\) and performs only (7.9), replacing \(B,D\) by
\(\sigma^tA,\sigma^tC\).  Their middle supports are disjoint because
(7.9) is supported on the old packet union \(B\sqcup D\), whereas (7.10)
is supported on \(A\sqcup C\).

### Relation to the balanced-\(C_8\) and anti-repair audits

Theorem 7.4 proves an ownership-level degree-two trade.  It does **not**
by itself prove that the symmetric difference of the two odd-graph
2-factors is one alternating 8-cycle.  In general, two factorizations of
the same \(2p\) vertices into two wreath cycles can have an odd-graph edge
symmetric difference consisting of several alternating even circuits.

If one of (7.9)--(7.10) additionally has a single alternating-\(C_8\)
edge realization, then the existing two-wreath theorem says its two old
cut-length profiles are balanced, and the universal four-cell depth-one
drift formula applies.  The proved canonical **anti-repair** theorem is
narrower still: it concerns the explicit private MSW common-core \(C_8\)
family.  Nothing in the column pairing equations identifies the trades
(7.9)--(7.10) with that private family.  Therefore the existing
anti-repair result does not rule out a useful length-four phase completion.

---

## 8. Ordinary shifts versus \(\{0,2\}\) partial counts

The same alternating vector appears in two different problems and must not
be conflated.

### Ordinary one-shift-per-row lift

Every row is selected exactly once.  On \(C\), the selected shift set is

\[
 A_i=
 \begin{cases}
 \{t\},&i\in C^+,\\
 \{-t\},&i\in C^-,
 \end{cases}
\qquad
 A_i=\{0\}\quad(i\notin C).
\tag{8.1}
\]

Under (5.4), each phase pair \((x,x+t)\) is swapped.

### Partial-orbit count direction

The real count kernel instead gives

\[
 r_i=
 \begin{cases}
 2,&i\in C^+,\\
 0,&i\in C^-,\\
 1,&i\notin C.
 \end{cases}
\tag{8.2}
\]

This satisfies \(Br=p\mathbf1\), but it does not specify which phases are
selected.  A partial-orbit completion chooses sets
\(A_i\subseteq\mathbb F_p\) with \(|A_i|=r_i\) and must satisfy

\[
 \boxed{
 \bigsqcup_{i\in N_j}(\phi_{ij}+A_i)=\mathbb F_p
 \quad\text{for every column }j,}
\tag{8.3}
\]

where the union is a disjoint multiset union.  Equation \(Br=p\mathbf1\)
checks only the cardinality of (8.3).

There is a special completion governed by the same pairing condition:

\[
 A_i=
 \begin{cases}
 \{0,t\},&i\in C^+,\\
 \varnothing,&i\in C^-,\\
 \{0\},&i\notin C.
 \end{cases}
\tag{8.4}
\]

At a paired column phase \(x\leftrightarrow x+t\), the doubled \(+\) row
retains the occurrence at \(x\) and adds the occurrence at \(x+t\), while
the \(-\) row at \(x+t\) is omitted.  Hence (8.4) satisfies (8.3) if and
only if (5.4) holds.

Thus the same phase-pairing array supports both

* a nonconstant ordinary phase lift, by swapping paired occurrences; and
* one particular \(\{0,2\}\) partial-count completion, by replacing every
  omitted occurrence with the second copy of its paired row.

But the two problems are not equivalent.  General partial completion may
choose arbitrary two-element shift sets on doubled rows and is governed by
(8.3), not by the ordinary-shift pairing theorem.  Therefore failure of
one ordinary exponent vector does not by itself rule out partial
completion.  Conversely the bounded count vector (8.2) by itself proves
only the zero-frequency equation and supplies no phase completion.

---

## 9. Exact status

Proved:

1. all power-sum equations are exactly the column permutation criterion
   (3.2);
2. for one alternating even-cycle direction, legality is equivalent to the
   transposition pairing \(X_j^-=X_j^++t\) in every column;
3. abstract singleton Latin arrays satisfying that condition always exist;
4. the first extra condition is the rowwise odd-graph/wreath constraint
   (7.2);
5. ordinary one-shift lifts and \(\{0,2\}\) partial counts have distinct
   variables, although the special completion (8.4) uses the same pairing.
6. every legal direction on a complement 2-cycle is a completely inert
   swap of two translate rows; the first potentially productive cycle has
   length at least four;
7. a longer-cycle legal direction cannot decompose into fixed translate
   pairs, because distinct rows have equal necklace neighborhoods exactly
   on complement 2-cycles.
8. a legal length-four direction is exactly two disjoint nontrivial
   two-for-two wreath trades for the ordinary lift, while the special
   partial completion performs one of them; being a universal or private
   alternating \(C_8\) requires additional odd-graph edge geometry.

Unproved: whether the phase arrays produced by the actual MSW/prime-cycle
wreath geometry realize (5.4) on a positive supply of \(p+2\) components,
or whether (7.2) forces a new obstruction.
