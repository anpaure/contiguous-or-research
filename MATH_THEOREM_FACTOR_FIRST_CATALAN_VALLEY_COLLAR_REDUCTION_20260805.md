# Factor-first Catalan valleys and the protected collar reduction

**Date:** 2026-08-05  
**Method:** pure mathematics; exact counting and local Johnson geometry;
no computation, search, or solver  
**Status:** unconditional reduction.  Once a lower-exact two-factor has
been chosen, every factor-extension Hall cut disappears.  An adjacent repeat
of one upper colour is exactly the left seam of a balanced pivot collar, and
a clean geodesic arm supplies the whole generalized collar.  The exact upper
repeat surplus is four times the asymptotic collar demand, so only a quarter
of the Catalan repeats need be localized, clean, and spaced.  Existence of
such a decorated factor is not proved here.

## 1. The projected factor

Put

\[
 n=2r-1,
 \qquad
 \mathcal L={ [n]\choose r-1},
 \qquad
 \mathcal U={ [n]\choose r},
 \qquad
 W=|\mathcal L|=|\mathcal U|.
\]

Let `F` be a simple spanning two-factor of the middle-level incidence
graph between `mathcal L` and `mathcal U`.  Suppress every lower vertex
`z`.  Its two owner neighbours are distinct sets

\[
 A=z+\{a\},\qquad B=z+\{b\},
\]

and give the Johnson edge `AB`, with lower colour `z=A cap B` and upper
colour `A union B`.

The projected graph `J(F)` is a spanning two-factor on the `W` owners.
Every rank-`(r-1)` lower colour occurs exactly once, because every lower
vertex of the incidence graph occurs exactly once.  Thus selecting `F`
first makes the owner/lower factor and all of its residual Hall cuts
automatic.

## 2. The exact Catalan repeat budget

There are

\[
 U={n\choose r+1}=W{r-1\over r+1}
\tag{2.1}
\]

rank-`(r+1)` upper colours.  The projected factor has exactly `W` Johnson
edges.  If it is upper-surjective, and `m_C` is the multiplicity of upper
colour `C`, then

\[
 \boxed{
 \sum_C(m_C-1)=W-U={2W\over r+1}=\operatorname {Cat}_r.}
\tag{2.2}
\]

The odd Catalan collar demand is

\[
 b={W\over2r-1}-1.
\tag{2.3}
\]

Consequently

\[
 {\operatorname {Cat}_r\over b}
 ={2W/(r+1)\over W/(2r-1)-1}
 =4+o(1).
\tag{2.4}
\]

Thus the upper-exact factor already contains four times the required
collar count in scalar repeat surplus.  The issue is not the number of
repeats, but their physical localization.

## 3. An upper valley is exactly a collar seam

Take three consecutive projected owners

\[
 P,M_0,M_1
\]

on an oriented component of `J(F)`.  Call `M_0` an **upper valley** if

\[
 P\cup M_0=M_0\cup M_1=:C.
\tag{3.1}
\]

Since the owners are distinct rank-`r` facets of the rank-`(r+1)` set
`C`, there are distinct labels `a,b,c in C` such that

\[
 P=C-\{a\},\qquad M_0=C-\{b\},\qquad M_1=C-\{c\}.
\tag{3.2}
\]

Put

\[
 \rho _1=b,\qquad q_-=a,\qquad \lambda _1=c.
\tag{3.3}
\]

Then

\[
 P=M_0-\{q_-\}+\{\rho _1\},
 \qquad
 M_1=M_0-\{\lambda _1\}+\{\rho _1\}.
\tag{3.4}
\]

Equations (3.1)--(3.4) are exactly the generalized balanced collar's
left seam: the seam edge and the first internal edge have one repeated
upper colour, while their lower colours are distinct.

### Lemma 3.1 (clean arm gives the full collar)

Continue from `M_1` along the oriented factor as

\[
 M_{j+1}=M_j-\{\lambda _{j+1}\}+\{\rho _{j+1}\}
 \qquad(1\le j<h),
\tag{3.5}
\]

and denote the following factor owner by `N`.  Assume

1. `lambda_1,...,lambda_h` are distinct;
2. `rho_1,...,rho_h` are distinct;
3. no `rho_i` is one of the `lambda_j`; and
4. the final transition has the form
   `N=M_h-{q_+}+{z}`, where `q_+` lies in the fixed core left after the
   two rails are removed and `z` is fresh.

Then

\[
 P,M_0,M_1,\ldots,M_h,N
\]

is exactly one generalized balanced pivot collar: the internal owners are
the Johnson geodesic

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
\tag{3.6}
\]

and the final edge is the generalized trace-compatible right endpoint.

#### Proof

Conditions 1--3 imply that all internal exchanges in (3.5) remove an
unused member of the initial owner and insert a fresh member of its
complement.  Removing the two rails from `M_0` leaves a fixed core `Q`,
and induction gives (3.6).  Equation (3.4) gives the authenticated left
seam.  Condition 4 says exactly that the next edge removes `q_+ in Q` and
inserts the fresh endpoint label `z`.  These are the defining identities
of the generalized collar. \(\square\)

The ordinary residence-separation condition must be stated with one explicit
exception here.  At an upper valley, `rho_1` is deleted on `P-M_0` and
immediately reinserted on `M_0-M_1`; this forced seam pair is precisely what
creates the repeated upper colour.  Hence a valley is clean when, after
exempting that one prescribed delete--reinsert pair, no rail label recurs in
the following `h+1` transitions, the deletion and insertion rails are
otherwise disjoint, and the terminal transition deletes a core label `q_+`
and inserts a fresh label `z` as in Condition 4.  A blanket hypothesis that
*every* successive insertion/deletion event is separated by more than `h`
would exclude the valley itself and therefore cannot certify this lemma.

## 4. A factor-first sufficient object

Call upper valleys **resource-disjoint** if their oriented owner intervals

\[
 P,M_0,M_1,\ldots,M_h,N
\]

are vertex-disjoint in the incidence factor.  Their lower resources are
then also disjoint, because every lower vertex occurs once in `F`.

### Theorem 4.1 (factor-first collar extraction)

Suppose an upper-surjective spanning two-factor `F` has `b`
resource-disjoint clean upper valleys.  Then `F` contains a protected bank
of exactly `b` generalized balanced pivot collars with pairwise disjoint
owner and lower resources.  No protected-factor extension theorem, no
orientation choice, and no residual DM/Hall audit is required.

#### Proof

Apply Lemma 3.1 at the chosen valleys.  Vertex-disjoint owner intervals
give disjoint owner resources, and the spanning incidence factor uses every
lower colour once, so their lower resources are disjoint.  Since all
collars are literal subpaths of the already spanning two-factor, the
protected bank is extended by `F` itself. \(\square\)

The full factor already supplies every immediate upper target, so repeated
upper colours inside the protected collars cause no additional palette
defect; they are precisely part of the Catalan repeat ledger (2.2).

## 5. The sharpened remaining factor target

The factor-extension problem may therefore be replaced by the following
constructive statement.

> **Quarter-spaced Catalan valley factor.**  Construct an upper-surjective,
> lower-exact spanning two-factor whose transition chronology is clean at
> deadline depth and in which at least
> `b=W/(2r-1)-1` of the `Cat_r` units of upper repeat surplus occur as
> pairwise resource-disjoint upper valleys.

Only asymptotically one quarter of the unavoidable upper repeat surplus is
needed.  This target couples precisely the three rows that the protected-
bank-first strategy separated:

1. factor existence and topology;
2. immediate upper decoration;
3. residence/geodesic collar cleanliness.

It does not yet include arbitrary-width upper witnesses or the terminal
literal common cap.  The theorem above is a reduction, not a proof that the
quarter-spaced valley factor exists.

## 6. Dependencies

1. the balanced middle-level incidence graph;
2. the generalized balanced collar identities from
   `MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`;
3. the exact Catalan upper-palette count.
