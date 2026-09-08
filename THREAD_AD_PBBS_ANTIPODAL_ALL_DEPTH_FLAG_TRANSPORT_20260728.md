# Thread AD: PBBS antipodal all-depth flags and the residence hit/avoid gate

Date: 2026-07-28

Status: pure-mathematical theorem package.  The all-depth trace identities,
finite-surgery ribbon, targetwise support criterion, and conditional
protected-witness theorem are proved.  Existence of the required PBBS port
system and the common owner extension are not proved.

## 0. Outcome and corrected scope

Put

\[
 K=[2m+1],\qquad
 W=\binom{2m+1}{m},\qquad
 B_m=\operatorname {Cat}_m=\frac{W}{2m+1}.
\]

There are three logically different issues.

1. **All-depth flag support is solved before surgery.**  The audited PBBS
   theorem gives, for every \(0\le q\le m\) and every
   \(S\in\binom K{m-q}\), a canonical PBBS \(q\)-edge interval whose
   intersection is \(S\), with load

   \[
   1\le\mu_q(S)\le\binom{2q+1}{q}.
   \]

2. **Component topology is asymptotically cheap.**  The PBBS factor has at
   most \(B_m\) components.  Keeping the components separate and paying
   their \(O(H)\) collars costs

   \[
   O(HB_m)=O(W/\sqrt m)=o(W)
   \]

   at \(H=\Theta(\sqrt m)\).  Thus Hamiltonizing the factor is not itself
   the asymptotic coefficient-one gate.

3. **Residence and exact owners are decisive.**  A useful port system must
   hit all native short-residence intervals, preserve or recreate at least
   one all-depth flag witness for every target, pass the new-seam residence
   tests, and—only for the exact finite formula—admit the common labelled
   owner/Hall extension.

The exact missing combinatorial condition is consequently a
**hit/avoid transversal**:

\[
\boxed{
\begin{array}{ll}
P\cap I\ne\varnothing
 &\text{for every native short-residence interval }I,\\[2mm]
\exists\,J\in\mathcal W_q(S)\text{ with }P\cap J=\varnothing
 &\text{for every required flag target }(q,S),
\end{array}}
\tag{0.1}
\]

followed by local legality of the new connector collars.  Here \(P\) is
the set of old directed successor slots changed by the surgery and
\(\mathcal W_q(S)\) is the family of canonical PBBS \(q\)-edge witnesses
for \(S\).

The PBBS load cap is in the wrong direction for proving (0.1): a target may
have load one.  Rankwise marginal balancing also does not prove (0.1).
At any fixed depth \(q\) satisfying
\(0\le\gamma_{q,x}\le e_q\) for every coordinate, the hypersimplex theorem
constructs a hole-free multiset with the prescribed size and point degrees.
In this package those inequalities have been verified for the frozen
\(k=15\) Hall-29 rows \(q=2,3\).  The theorem supplies neither simultaneous
feasibility across depths nor a chronology or owner extension.

The odd-Hamiltonian formulas below use the standing assumption that \(W\)
is odd, which holds at \(k=15\).  Section 9 imports a separate PBBS
factor theorem valid for general \(m\); its asymptotic conclusion does not
assume that one odd-graph Hamilton cycle admits the step-two antipodal
enumeration used in Sections 1--2.

No constant-one theorem or exact \(k=15\) word is claimed here.

## 1. Odd-graph notation

Let

\[
 A_0,A_1,\ldots,A_{W-1},A_0
\]

be a Hamilton cycle in the odd graph

\[
 O_m=KG(2m+1,m).
\]

For the edge \(A_jA_{j+1}\), let \(z_j\) be the unique omitted label:

\[
 z_j\in K\setminus(A_j\cup A_{j+1}).
\]

Then

\[
 A_{j+1}=\overline{A_j}\setminus\{z_j\},
\tag{1.1}
\]

\[
 A_{j+2}=A_j-\{z_{j+1}\}+\{z_j\}.
\tag{1.2}
\]

Assume \(W\) is odd, as in \(k=15\).  Put

\[
 B_i=A_{2i},
\qquad
 T_i=\overline{A_{2i-1}}.
\tag{1.3}
\]

Multiplication by two permutes \(\mathbb Z_W\).  Hence \(B\) enumerates all
rank-\(m\) sets and \(T\) enumerates all rank-\((m+1)\) sets.  Moreover

\[
 B_i=T_i\cap T_{i+1},
\tag{1.4}
\]

\[
 T_{i+1}
 =T_i-\{z_{2i-1}\}+\{z_{2i}\}.
\tag{1.5}
\]

For \(q\ge0\), define the cyclic lower and upper traces of \(T\) by

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h},
\qquad
 U_i^{(q)}=\bigcup_{h=0}^{q}T_{i+h}.
\tag{1.6}
\]

No residence assumption is made in Sections 1--5.

## 2. Every trace is one odd-graph step-two interval

For \(q\ge1\), define the descending odd-graph flag

\[
 F_i^{(q)}
 =\bigcap_{h=0}^{q-1}B_{i+h}.
\tag{2.1}
\]

### Theorem 2.1 (exact all-depth \(A/z\) formula)

For every \(q\ge1\),

\[
\boxed{
 F_i^{(q)}
 =B_i\setminus
 \{z_{2i+1},z_{2i+3},\ldots,z_{2i+2q-3}\}.}
\tag{2.2}
\]

Equivalently, for every \(q\ge1\),

\[
\boxed{
 L_i^{(q)}
 =T_i\setminus
 \{z_{2i-1},z_{2i+1},\ldots,z_{2i+2q-3}\},}
\tag{2.3}
\]

and, for every \(q\ge0\),

\[
\boxed{
 U_i^{(q)}
 =T_i\cup
 \{z_{2i},z_{2i+2},\ldots,z_{2i+2q-2}\}.}
\tag{2.4}
\]

Repeated labels in these displays are interpreted setwise.  The identities
hold even when a trace has the wrong nominal rank.

### Proof

The step-two transition (1.2) deletes \(z_{2i+1}\) from \(B_i\) and inserts
\(z_{2i}\).  A coordinate of the initial \(B_i\) belongs to every one of

\[
 B_i,B_{i+1},\ldots,B_{i+q-1}
\]

if and only if it is never among the displayed deletion labels.  This proves
(2.2), without requiring those labels to be distinct.

Likewise, a coordinate of \(T_i\) belongs to every
\(T_i,\ldots,T_{i+q}\) precisely when it is never among the \(q\) deletion
labels in (2.3).  A coordinate belongs to their union precisely when it was
already in \(T_i\) or appears among the \(q\) insertion labels in (2.4).
\(\square\)

### Theorem 2.2 (one flag row serves both shores)

For every \(q\ge1\),

\[
\boxed{L_i^{(q)}=F_i^{(q)}.}
\tag{2.5}
\]

There is a fixed cyclic shift \(s\), determined by

\[
 2s\equiv-1\pmod W,
\tag{2.6}
\]

such that

\[
\boxed{\overline{U_i^{(q-1)}}=F_{i+s}^{(q)}.}
\tag{2.7}
\]

Consequently, as multisets,

\[
\boxed{
\{\!\{L_i^{(q)}:i\in\mathbb Z_W\}\!\}
=
\{\!\{F_i^{(q)}:i\in\mathbb Z_W\}\!\}
=
\{\!\{\overline{U_i^{(q-1)}}:i\in\mathbb Z_W\}\!\}.}
\tag{2.8}
\]

### Proof

Since \(B_i=T_i\cap T_{i+1}\),

\[
 \bigcap_{h=0}^{q-1}B_{i+h}
 =\bigcap_{h=0}^{q}T_{i+h}=L_i^{(q)},
\]

which proves (2.5).  De Morgan and (1.3) give

\[
 \overline{U_i^{(q-1)}}
 =\bigcap_{h=0}^{q-1}A_{2i+2h-1}.
\]

The right side is \(F_{i+s}^{(q)}\) after the shift (2.6).
Equation (2.8) follows because cyclic shifts preserve multisets.
\(\square\)

### Corollary 2.3 (single all-depth flag-cover gate)

The cyclic antipodal lift is upper-universal at every rank if and only if

\[
\boxed{
\{F_i^{(q)}:i\in\mathbb Z_W\}
\supseteq\binom K{m-q+1}
\quad(1\le q\le m+1).}
\tag{2.9}
\]

The same rows simultaneously give complete lower depth-\(q\) support.
Thus \(q=2\) turn-surjectivity is only the first nontrivial row of one
all-depth flag-cover problem.

For a target \(R\in\binom K{m-q+1}\), (2.2) gives the exact occurrence
criterion:

\[
 F_i^{(q)}=R
\]

if and only if the \(q-1\) odd-offset labels in (2.2) are a
repetition-free ordering of \(B_i\setminus R\).

## 3. The authoritative PBBS input

Let \(g\) denote the directed PBBS step-two successor on

\[
 \mathcal V=\binom K m.
\]

It is a permutation whose cycles form the projected PBBS factor.  For
\(0\le q\le m\), put

\[
 \Phi_q(x)=\bigcap_{h=0}^{q}g^h(x),
\tag{3.1}
\]

and

\[
 \Omega_q(S)=\{x\in\mathcal V:\Phi_q(x)=S\}.
\tag{3.2}
\]

The audited PBBS all-depth corridor theorem says:

### Theorem 3.1 (frozen PBBS flag factor)

For every \(0\le q\le m\) and every
\(S\in\binom K{m-q}\),

\[
\boxed{
 1\le|\Omega_q(S)|\le\binom{2q+1}{q}.}
\tag{3.3}
\]

Each \(x\in\Omega_q(S)\) gives a canonical oriented \(q\)-edge PBBS path

\[
 x,gx,\ldots,g^q x
\]

whose full intersection is \(S\).

The upper bound in (3.3) is not a redundancy theorem.  In particular,
\(|\Omega_q(S)|\) may equal one.  Nothing in (3.3) implies that an arbitrary
port set leaves one occurrence alive.

The published lexical Middle-Levels Hamiltonization does not apply to this
factor.  Its alternating hexagons are proved relative to the distinct
lexical factor, and the two factors already have different component counts
at \(m=2\).  A PBBS connector theorem must therefore be proved on the PBBS
factor itself.

## 4. Exact finite-surgery ribbon

Let \(\widehat g\) be another directed permutation of \(\mathcal V\), and
put

\[
 P=\{x\in\mathcal V:\widehat g(x)\ne g(x)\}.
\tag{4.1}
\]

The elements of \(P\) are the changed old projected successor slots.  Define

\[
 \mathcal C_q(P)=
 \bigcup_{a=0}^{q-1}g^{-a}P
 \qquad(q\ge1),
\qquad
 \mathcal C_0(P)=\varnothing.
\tag{4.2}
\]

### Theorem 4.1 (all-depth finite-surgery locality)

If \(x\notin\mathcal C_q(P)\), then

\[
 \widehat g^h(x)=g^h(x)
 \qquad(0\le h\le q),
\tag{4.3}
\]

and therefore

\[
 \Phi_q^{\widehat g}(x)=\Phi_q^g(x).
\tag{4.4}
\]

Consequently

\[
\boxed{
\#\{\text{changed depth-}q\text{ occurrences}\}
\le q|P|,}
\tag{4.5}
\]

\[
\boxed{
\|\widehat\mu_q-\mu_q\|_1\le2q|P|,}
\tag{4.6}
\]

and the number of formerly covered depth-\(q\) targets which become holes
is at most

\[
\boxed{q|P|.}
\tag{4.7}
\]

### Proof

For \(x\notin\mathcal C_q(P)\), none of

\[
 x,gx,\ldots,g^{q-1}x
\]

is a port.  Induct on \(h\).  If
\(\widehat g^h(x)=g^h(x)\) for \(h<q\), their common value is not in \(P\),
so applying the two successors gives the same next vertex.  This proves
(4.3) and hence (4.4).

Since \(g\) is a permutation, every \(g^{-a}P\) has size \(|P|\), proving
(4.5).  Replacing one occurrence changes its histogram by a vector of
\(\ell^1\)-norm at most two, proving (4.6).  Deleting one occurrence can
create at most one hole, proving (4.7).  \(\square\)

### Exact ribbon form

On one oriented component of length \(v\), for \(1\le q<v\), a changed
edge at phase \(r\) affects exactly the \(q\) old \(q\)-edge starts

\[
 r-q+1,r-q+2,\ldots,r.
\tag{4.8}
\]

For \(1\le H<v\), through depths \(1,\ldots,H\), it therefore creates the
triangular ribbon

\[
 \mathfrak R_H(r)
 =\{(q,i):1\le q\le H,\ r-q+1\le i\le r\},
\tag{4.9}
\]

of size

\[
 |\mathfrak R_H(r)|=\frac{H(H+1)}2.
\tag{4.10}
\]

For several ports on components longer than \(H\), the exact
destroyed-start set is the union of these ribbons; overlaps are subtracted
literally.  Without any component-length assumption, Theorem 4.1 still
gives the safe bound that a directed alternating \(C_{2t}\) changing \(t\)
projected successor slots affects at most \(tq\) old depth-\(q\)
occurrences.  A hexagon therefore gives \(3q\), not \(6q\), in the
projected-slot convention.

If one instead edits \(t\) raw odd-graph successor slots and only afterwards
projects through the square of that successor, at most \(2t\) projected
slots can change.  These two conventions must not be mixed.

## 5. Exact targetwise flag transport

Partitioning the start set into \(\mathcal C_q(P)\) and its complement gives
an equality, not only a bound.

### Theorem 5.1 (signed connector identity)

For every \(q\) and every target \(S\),

\[
\boxed{
\widehat\mu_q(S)
=
|\Omega_q(S)\setminus\mathcal C_q(P)|
+
|\{x\in\mathcal C_q(P):
          \Phi_q^{\widehat g}(x)=S\}|.}
\tag{5.1}
\]

Hence at least one unchanged old PBBS witness preserves \(S\) if and only if

\[
\boxed{
\Omega_q(S)\setminus\mathcal C_q(P)\ne\varnothing.}
\tag{5.2}
\]

Equivalently, \(P\) is not a transversal of the family of \(q\)-edge
PBBS witness paths

\[
 \bigl\{\{x,gx,\ldots,g^{q-1}x\}:x\in\Omega_q(S)\bigr\}.
\tag{5.3}
\]

If (5.2) fails, the target is still restored precisely when one of the new
connector-ribbon flags in the second term of (5.1) equals \(S\).

### Proof

Outside \(\mathcal C_q(P)\), Theorem 4.1 identifies the new occurrence with
the old one.  Inside it, count the new flags directly.  This is exactly
(5.1), from which the rest follows.  \(\square\)

### Protected-witness form

Choose one canonical PBBS occurrence for every required \((q,S)\).  If every
chosen \(q\)-edge path avoids \(P\), then every selected witness survives
unchanged.  This condition is inductive under a merge tree: at each node,
one may reassign a target to another live occurrence before selecting the
next ports.

If the oriented deletion ladder itself, rather than only its full
intersection, must be preserved, protected segments must retain their
orientation.  Reversing a segment preserves full-window intersections and
unions, but changes a prefix flag into a suffix flag.

### Theorem 5.2 (exact two-endpoint cut grid)

Let \(T=(T_i)_{i\in\mathbb Z_v}\) be one directed owner cycle of length
\(v\).  Cut it between \(T_{-1}\) and \(T_0\), and define its left and
right endpoint flags by

\[
 Q_t^-=\bigcap_{j=-t}^{-1}T_j,\qquad
 Q_u^+=\bigcap_{j=0}^{u-1}T_j,
 \tag{5.4}
\]

and

\[
 R_t^-=\bigcup_{j=-t}^{-1}T_j,\qquad
 R_u^+=\bigcup_{j=0}^{u-1}T_j.
 \tag{5.5}
\]

For every \(1\le q<v\), the lost lower and upper depth-\(q\) windows are
exactly

\[
 \boxed{
 L_{-t}^{(q)}=Q_t^-\cap Q_{q+1-t}^+,qquad
 U_{-t}^{(q)}=R_t^-\cup R_{q+1-t}^+
 }
 \quad(1\le t\le q).
 \tag{5.6}
\]

Thus, for \(1\le H<v\), one cut exposes through depth \(H\) the triangular
antidiagonal grid

\[
 \{(t,u):t,u\ge1,\ t+u\le H+1\},
 \tag{5.7}
\]

with exactly \(H(H+1)/2\) lost starts on either shore before coincidences
of target colours are identified.

#### Proof

A \(q\)-edge window crosses the cut precisely when it has \(t\) owners to
the left and \(q+1-t\) owners to the right, for one and only one
\(t\in\{1,\ldots,q\}\).  Taking its intersection or union gives (5.6).
Summing the \(q\) starts for \(1\le q\le H\) gives (5.7) and
\(1+\cdots+H=H(H+1)/2\).  \(\square\)

Theorem 5.2 is an exact localization, not an owner theorem.  Separate
availability of the two endpoint chains does not by itself produce a
literal word realizing all mixed meets \(Q_t^-\cap Q_u^+\), and pointwise
or rankwise balance does not supply their common owners.  A seam chart must
realize this antidiagonal grid with the same physical endpoint states.

## 6. Exact residence transport

Write a directed middle transition as

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\tag{6.1}
\]

### Lemma 6.1 (odd-distance residence)

Depth-\(d\) residence is equivalent to

\[
\boxed{
 b_i\ne a_{i+t}\qquad(1\le t\le d)}
\tag{6.2}
\]

at every internal index.  In the antipodal omitted-label word this is

\[
\boxed{
 z_j\ne z_{j+s}
 \quad\text{for every odd }s\in\{1,3,\ldots,2d-1\}.}
\tag{6.3}
\]

### Proof

The element \(b_i\) is inserted at transition \(i\).  If it is deleted at
transition \(i+t\), its internal one-run has length \(t\).  Excluding
\(t\le d\) is exactly (6.2).  Formula (1.5) identifies insertion and
deletion labels with the two parity classes of \(z\), giving (6.3).
\(\square\)

For each violation \(b_i=a_{i+t}\), \(1\le t\le d\), define the cyclic
projected-slot interval

\[
 I_{i,t}=\{i,i+1,\ldots,i+t\}.
 \tag{6.4}
\]

It contains the insertion slot \(i\), every intervening slot, and the
removal slot \(i+t\).  Thus \(|I_{i,t}|=t+1\), although the positive
coordinate run has length \(t\).  Put

\[
 \mathcal I_d
 =\{I_{i,t}:b_i=a_{i+t},\ 1\le t\le d\}.
 \tag{6.5}
\]

Changing any slot in \(I_{i,t}\) prevents that old insertion and removal
from lying in one retained path segment.

### Theorem 6.2 (residence-local seam criterion)

Suppose:

1. \(P\) meets every interval in \(\mathcal I_d\); and
2. every new connector seam satisfies every comparison
   \(b_i\ne a_{i+t}\), \(1\le t\le d\), whose transition window crosses
   that seam.

Then every final segment or rethreaded chronology is depth-\(d\) resident.
Conversely, both conditions are necessary if no internal segment is otherwise
edited.

### Proof

Any old short run whose interval avoids \(P\) remains intact, proving
necessity of the first condition.  After all intervals in
\(\mathcal I_d\) are hit, every retained segment is internally resident.
Any new short run in the rethreaded chronology must cross a new seam, where
the second condition excludes it.  The converse is immediate.  \(\square\)

For a splice whose only new raw-\(z\) comparisons meet one
length-\(\ell\) collar or cross one of its two boundary seams, every new
comparison lies in the radius-\(d\) connector ribbon.  There are at most

\[
 d\ell+d^2
\tag{6.6}
\]

candidate odd-offset pairs.  Thus residence is a genuinely local connector
audit after the native short-return intervals have been cut.

## 7. The combined protected-flag/residence theorem

### Theorem 7.1 (conditional PBBS rethreading theorem)

Let \(g\) be the directed PBBS step-two factor.  Suppose an
orientation-coherent physical rethreading produces a directed successor
\(\widehat g\) with port set \(P\).  Here *physical* means that every new
edge \(X\to Y\) is a legal Johnson edge, its rank-\((m+1)\) collar
\(X\cup Y\) has the asserted orientation, and the resulting components can
be read as actual middle chronologies.  Assume:

1. **Residence transversal:** \(P\) meets every native interval in
   \(\mathcal I_d\).
2. **Flag nontransversality:** for every required
   \(0\le q\le m\) and
   \(S\in\binom K{m-q}\),

   \[
   \Omega_q(S)\setminus\mathcal C_q(P)\ne\varnothing,
   \tag{7.1}
   \]

   or a new connector flag supplies \(S\) through the second term of (5.1).
3. **Seam residence:** every new seam passes the direct tests (6.2);
   in a complement-antipodal lift these may equivalently be audited as the
   odd-distance tests (6.3).
4. **Physical orientation:** protected oriented ladders are not reversed
   unless the corresponding suffix ladder is explicitly accepted.

Then the rethreaded chronology is depth-\(d\) resident and retains the
complete PBBS all-depth flag support.

If the rethreading remains complement-antipodal, Theorem 2.2 turns that one
flag support into both complete lower and complete upper trace support.
If it breaks antipodal symmetry, the lower and upper physical witness
families must instead be protected separately; no abstract complement
inference is then valid.

### Proof

Theorem 5.1 and hypothesis 2 preserve or recreate every flag target.
Theorem 6.2 and hypotheses 1 and 3 give residence.  Physical legality and
hypothesis 4 interpret the successor components as integral directed
Johnson chronologies.  The last paragraph is exactly Theorem 2.2, with its
symmetry hypothesis retained.  \(\square\)

This is a conditional theorem, not an existence proof.  Its old-witness-only
core is the hit/avoid system (0.1).  It also does not assert the labelled
owner/Hall extension.  If that extension is needed, the collars
\(X\cup Y\), their ordering, and the emitted seam letters must satisfy it as
an additional hypothesis.  If complement-antipodality is invoked, one must
further exhibit an odd-graph successor \(\widehat f\) with
\(\widehat g=\widehat f^{\,2}\); an arbitrary legal Johnson rethreading does
not have that consequence.

## 8. Literal band consequence and the unprotected \(Q^2\) loss

Assume \(1\le Q\le m\), and that the final chronology is one cyclic
rank-\((m+1)\) Johnson chronology
\(T=(T_i)_{i\in\mathbb Z_W}\) and is depth-\(Q\) resident.  Define its
maximal cyclic erosion letters

\[
 E_j=\bigcap_{h=0}^{Q}T_{j-h}.
 \tag{8.1}
\]

### Theorem 8.1 (literal all-depth erosion identity)

Every \(E_j\) is nonempty, and for every \(0\le q\le Q\),

\[
 \boxed{
 L_i^{(q)}=\bigcup_{j=i+q}^{i+Q}E_j,\qquad
 U_i^{(q)}=\bigcup_{j=i}^{i+Q+q}E_j.}
 \tag{8.2}
\]

Consequently the literal word

\[
 E_0,E_1,\ldots,E_{W-1},E_0,E_1,\ldots,E_{2Q-1}
 \tag{8.3}
\]

has length \(W+2Q\) and realizes, as contiguous ORs, every cyclic lower and
upper trace of depth at most \(Q\).

#### Proof

Fix a coordinate.  If its cyclic \(T\)-indicator is identically zero or
identically one, both identities are immediate.  Otherwise choose one of
its cyclic positive runs \([a,b]\).  Depth-\(Q\) residence says that this
run has length at least \(Q+1\).  Its positive run in the eroded word \(E\)
is therefore exactly \([a+Q,b]\).  The interval \([i+q,i+Q]\) meets
\([a+Q,b]\) if and only if

\[
 i\ge a,\qquad i+q\le b,
\]

which is exactly the condition that the coordinate belong to every one of
\(T_i,\ldots,T_{i+q}\).  Similarly, \([i,i+Q+q]\) meets
\([a+Q,b]\) if and only if

\[
 i\le b,\qquad i+q\ge a,
\]

which is exactly the condition that the coordinate belong to at least one
of those owners.  This proves (8.2) coordinatewise.  Repeating the first
\(2Q\) erosion letters makes every displayed cyclic interval an honest
linear interval.  Finally, each \(E_j\) is an intersection of \(Q+1\)
rank-\((m+1)\) owners across \(Q\) Johnson transitions, so it has at least
\(m+1-Q>0\) elements.  \(\square\)

Now assume in addition that \(T\) is a complement-antipodal Hamilton
chronology, so its rank-\((m+1)\) owner row is already complete.  Let \(h_q\)
be the number of holes in the row \(F^{(q)}\), where \(F^{(q)}\) uses \(q\)
consecutive \(B\)-vertices.  For a missing \(F^{(q)}\)-target \(S\), append
\(S\) for the corresponding missing lower rank and append \(\overline S\)
for the corresponding missing upper rank whenever that shore lies in the
band.  Theorem 2.2 and Theorem 8.1 give the safe ledger

\[
\boxed{
L_Q\le
W+2Q+h_1+2\sum_{q=2}^{Q}h_q+h_{Q+1}.}
\tag{8.4}
\]

Thus, when all these flag rows are complete, the word covers every target
in the rank band \(m+1-Q,\ldots,m+1+Q\).

The row \(F^{(1)}\) contributes only its lower rank because the central
\(T\)-row is independently complete; \(F^{(Q+1)}\) contributes only the
outer upper rank.  Every intermediate row serves a lower and a complemented
upper rank.  (For a cyclic complement-antipodal Hamilton chronology,
\(h_1=0\) in any case.)

If the PBBS rows were initially complete and the rethreading changes
\(\delta=|P|\) projected successor slots, Theorem 4.1 gives

\[
 h_q\le(q-1)\delta.
\]

Substitution in (8.4) yields the exact safe bound

\[
\boxed{L_Q\le W+2Q+\delta Q^2.}
\tag{8.5}
\]

Thus an unprotected \(O(B_m)=O(W/m)\)-slot Hamiltonization is harmless only
for

\[
 Q=o(\sqrt m).
\]

At Gaussian depth it can have order-\(W\) repair cost.  The protected-witness
condition, or a shared linear seam chart, is essential there.  The PBBS
multiplicity cap alone gives neither.

Equation (8.5) is an upper bound for a one-cycle literalization, not an
argument that one cycle is needed asymptotically.

## 9. Connector topology is not the asymptotic gate

For the separate PBBS components and \(2H\le m+1\), the proved
dominance-staircase ledger is

\[
\boxed{
L_H\le
W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{9.1}
\]

Here \(\nu_H(P_m)\) is the maximum packing of edge-disjoint native
short-residence intervals.  At

\[
H_A=\lceil A\sqrt m\rceil
\]

the component-collar term is

\[
2H_AB_m=O_A(W/\sqrt m)=o_A(W).
\tag{9.2}
\]

Therefore merely merging the at most \(B_m\) PBBS components does not attack
the decisive asymptotic term.  The actual sufficient residence threshold is

\[
\boxed{\nu_{H_A}(P_m)=o_A(B_m\sqrt m)
\quad\text{for every fixed \(A>0\), as \(m\to\infty\)},}
\tag{9.3}
\]

the proved short-transversal gate.

A merge theorem is asymptotically useful only if its ports form a small
residence transversal, thereby proving or improving (9.3), or if it supplies
owner-compatible structure unavailable to the separate-cut word.  A theorem
whose sole conclusion is Hamiltonicity adds no asymptotic power.

For the exact finite formula, the distinction is different: component seams
consume a finite palette and interact with endpoint owners.  There one may
need a connected chronology, but Theorem 7.1 still does not supply the
labelled owner extension.

## 10. Relation to the hypersimplex completion theorem

For a fixed depth \(q\), the defect-transport law prescribes an excess-degree
vector \(\gamma_q\).  The new hypersimplex theorem proves that whenever

\[
0\le\gamma_{q,x}\le e_q,
\]

one copy of every target plus \(e_q\) uniform excess blocks realizes exactly
the required trace point degrees.  Symmetric two-block exchanges connect
that hole-free multiset to the actual trace multiset with the same
marginals.

At \(k=15\), the frozen Hall-29 data satisfy

\[
\gamma_{2,x}\in[568,574]\subset[0,1428],
\]

\[
\gamma_{3,x}\in[1138,1147]\subset[0,3429].
\]

Thus the observed depth-two and depth-three holes are not marginal
obstructions.  The theorem does not show that chosen hole-free completions
at the two depths can be realized simultaneously by one transition word.
Even such a chronology would still require a separate common owner/Hall
extension for the exact formula.

The remaining chronology condition has the following exact, purely integral
form.

### Theorem 10.1 (simultaneous row-ordering criterion)

Fix a finite ground set \(K\) and integers

\[
 N\ge2,\qquad 1\le d\le\min\{r,N-1\},\qquad r\le |K|.
 \tag{10.1}
\]

For \(0\le q\le d\), let \(\mathcal M_q\) be a multiset of \(N-q\)
members of \(\binom K{r-q}\).  There is a depth-\(d\) resident directed
Johnson chronology

\[
 T_0,T_1,\ldots,T_{N-1}
 \tag{10.2}
\]

whose depth-\(q\) lower-trace multiset is \(\mathcal M_q\) for every
\(q\le d\) if and only if the blocks of every \(\mathcal M_q\) admit
orderings

\[
 R_0^{(q)},R_1^{(q)},\ldots,R_{N-q-1}^{(q)}
 \tag{10.3}
\]

with both of the following properties:

1. the exact tower recurrence holds,

   \[
   \boxed{
   R_i^{(q+1)}
   =R_i^{(q)}\cap R_{i+1}^{(q)}
   }
   \quad
   (0\le q<d,\ 0\le i<N-q-1);
   \tag{10.4}
   \]

2. writing

   \[
   \{a_i\}=R_i^{(0)}\setminus R_{i+1}^{(0)},\qquad
   \{b_i\}=R_{i+1}^{(0)}\setminus R_i^{(0)}
   \quad(0\le i\le N-2),
   \tag{10.5}
   \]

   the finite-memory inequalities

   \[
   \boxed{
   b_i\ne a_{i+t}
   \quad
   (1\le t\le d,\ 0\le i\le N-2-t)
   }
   \tag{10.6}
   \]

   hold.

If \(d\le\min\{r-1,N-2\}\), compatible rank-\((r-d-1)\) rows are also
specified, and (10.4) holds through \(q=d\), then (10.6) follows
automatically.  The chronology is a graph-theoretic Johnson path if and
only if the states \(R_i^{(0)}\) are pairwise distinct; it is Hamilton when,
in addition,

\[
 N=\binom{|K|}{r},
 \qquad
 \mathcal M_0=\binom K r.
 \tag{10.7}
\]

#### Proof

For a resident directed Johnson chronology, set
\(R_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}\).  The iterated-intersection identity
gives (10.4), and residence gives (10.6).

Conversely, set \(T_i=R_i^{(0)}\).  Because
\(R_i^{(1)}=T_i\cap T_{i+1}\) has rank \(r-1\), consecutive \(T_i\)'s differ
by the singletons (10.5), so \(T\) is a directed Johnson chronology.
Induction on \(q\) using (10.4) gives

\[
 R_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}.
 \tag{10.8}
\]

Thus its row multisets are exactly the prescribed \(\mathcal M_q\), and
(10.6) is precisely depth-\(d\) residence.  Pairwise distinctness is
exactly the graph-theoretic path condition, and (10.7) then says that every
rank-\(r\) vertex occurs once.

For the last assertion, suppose \(b_i=a_{i+t}\) with \(1\le t\le d\).
In the \(t+1\) transitions from \(T_i\) through \(T_{i+t+1}\), the final
deleted label \(a_{i+t}=b_i\) was not in \(T_i\).  Hence at most \(t\)
elements of \(T_i\) are deleted, and their intersection has rank at least
\(r-t\), strictly larger than the required rank \(r-(t+1)\) in row
\(t+1\).  This contradicts (10.4) through row \(d+1\).  \(\square\)

The hypersimplex theorem supplies the multisets
\(\mathcal M_q^*\) separately; it supplies no orderings (10.3), no adjacent
recurrences (10.4), and no common deletion word (10.5).  The exact frozen
Hall-29 problem at \(q=2,3\) is to choose its degree-correct, hole-free
\(\mathcal M_2^*,\mathcal M_3^*\) so that they extend the fixed shallower
rows through (10.4)--(10.6), then satisfy the upper and owner conditions.
This is the **simultaneous hypersimplex-lift problem**.

A port surgery changes all rows through one successor map, but it becomes a
hypersimplex lift only after target multisets \(\mathcal M_q^*\) are
specified and its induced rows are required to equal them with their
prescribed marginals.  Theorem 7.1 imposes only support survival or
recreation; a port surgery may change the marginals, so the hit/avoid theorem
alone is not a hypersimplex-lift theorem.  Another rankwise balancing lemma
cannot solve either chronology problem.

## 11. Sharp obstruction to full-depth residence

The all-depth support theorem is selective: every target has some good
phase.  It must not be strengthened to depth-\(m\) residence of a Hamilton
antipodal chronology.

### Theorem 11.1 (depth-\(m\) residence is impossible)

Under the standing odd-\(W\) hypothesis, for \(m\ge2\), no Hamilton
odd-graph cycle has an antipodal lift of depth-\(m\) residence.

### Proof

Fix \(x\in K\).  Exactly
\(I=\binom{2m}{m-1}\) odd-graph vertices contain \(x\), and adjacent
vertices are disjoint, so the cyclic \(x\)-indicator has no \(11\) edge.
An edge has colour \(x\) exactly when its two endpoint indicators are
\(00\).  Hence the number of \(x\)-coloured edges is

\[
 W-2I
 =\binom{2m+1}{m}-2\binom{2m}{m-1}
 =C_m.
 \tag{11.1}
\]

Also

\[
W=(2m+1)C_m.
\tag{11.2}
\]

Consecutive occurrences of \(x\) are separated by an odd number of edges:
away from an \(x\)-labelled edge, membership of \(x\) toggles across each
odd-graph edge, and both endpoints of an \(x\)-labelled edge omit \(x\).

Depth-\(m\) residence and (6.3) forbid equal colours at every positive odd
gap at most \(2m-1\).  Hence every consecutive \(x\)-gap is at least
\(2m+1\).  Its average is

\[
\frac W{C_m}=2m+1,
\]

so every gap equals \(2m+1\).  Thus the whole \(z\)-word is
\((2m+1)\)-periodic, with one occurrence of every colour in each period.

Across one period, membership of any fixed coordinate toggles on the other
\(2m\) edges, an even number.  Therefore

\[
A_{j+2m+1}=A_j.
\]

This contradicts Hamiltonicity because
\(W=(2m+1)C_m>2m+1\) for \(m\ge2\).  \(\square\)

Hence all-depth flag support must coexist with deep stalls and repeated
deletion labels.  The correct quantifier is “one surviving good interval
per target,” exactly as in (7.1), not “every phase is a strict flag.”

## 12. Precise remaining theorem

The proved statements reduce the PBBS-antipodal lane to the following
existence problem.

> **PBBS residence/flag/owner transport theorem (open).**  For the required
> depth \(d\) or band height \(H\), choose a physically feasible directed
> port system \(P\) and connector ordering such that:
>
> 1. \(P\) hits every native short-residence interval;
> 2. \(P\) does not hit every canonical PBBS witness of any required flag
>    target, except where a new connector flag replaces that target;
> 3. every new connector collar satisfies the direct residence tests,
>    equivalently the odd-distance tests when the lift remains antipodal;
> 4. the resulting simultaneous flag trades admit the common trace-two
>    owner/Hall extension and all private-hit conditions.

For asymptotic coefficient one, this four-item rethreading theorem is not
necessary: if the separate-cut residence packing meets (9.3), the already
proved dominance-staircase word repairs the cut traces at \(o(W)\) cost.
Neither Hamiltonization nor an old-witness-preserving port system is then
required.  For the exact finite formula, all four rethreading items remain
coupled.

For PBBS support and residence, the remaining port gate is the simultaneous
hit/avoid chronology, while the separate-cut asymptotic route asks only for
the packing estimate (9.3).  For the verified frozen Hall-29 rows \(q=2,3\),
point-degree balance and the rankwise exchange lattice are not obstructions;
their remaining gate is the simultaneous ordering problem
(10.4)--(10.6).  The exact finite problem additionally requires the common
owner lift.  These implications are distinct.

## 13. Independent audit points

The following constants and scopes were checked separately.

1. \(F^{(q)}\) uses \(q\) \(B\)-vertices and \(q-1\) successor edges.
   Radius \(Q\) needs rows \(F^{(1)},\ldots,F^{(Q+1)}\).
2. Changing \(\delta\) projected successor slots changes at most
   \(\delta(q-1)\) occurrences in row \(F^{(q)}\).
3. A projected \(C_6\) changes three successor slots.  The factor two arises
   only when raw odd-graph slots are changed before step-two projection.
4. The paired-band singleton-repair ledger is exactly \(\delta Q^2\), not
   \(2\delta Q^2\).
5. Reversal preserves a full-window intersection/union but reverses the
   ordered flag ladder.
6. After antipodal symmetry is broken, lower and upper physical witnesses
   must be protected separately.
7. The PBBS load estimate is an upper cap and provides no minimum redundancy.
8. The published lexical connector theorem is not a PBBS connector theorem.
9. Pure component collars cost \(O(HB_m)=o(W)\) at Gaussian height.
10. The exact finite owner/Hall gate is not implied by all-depth support,
    residence, or hypersimplex marginal completion.
11. The dominance-staircase ledger (9.1) assumes \(2H\le m+1\), which holds
    eventually for fixed-\(A\) Gaussian height.
12. Hypersimplex completion is conditional on
    \(0\le\gamma_{q,x}\le e_q\); in this package it has been numerically
    verified only for the frozen Hall-29 rows \(q=2,3\).
13. Exact cut-ribbon counts require depth smaller than the affected cycle
    length; Theorem 4.1's \(q|P|\) bound remains safe without that
    hypothesis.
14. Ordered rows through depth \(d\) do not encode a residence collision at
    delay exactly \(d\); either (10.6) or one additional correct-rank row is
    necessary.
15. A support-preserving port surgery is not automatically a hypersimplex
    lift, because it need not realize any preselected degree-correct row
    multiset.
