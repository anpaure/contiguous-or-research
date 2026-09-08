# Owner-aware twelve-top source allocation: closed installation, exact leave, and the physical augmenting-rank gate

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, web input,
or probabilistic existence theorem is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and let

\[
 \mathcal U=\binom{[n]}M,\qquad
 \mathcal X=\binom{[n]}m,\qquad
 N=|\mathcal U|,\qquad W=|\mathcal X|.
\tag{0.2}
\]

Let \(T\) be a full coefficient-one table: it has one literal rooted
length-\(d\) tight-window row \(t_U\) on every \(U\in\mathcal U\), and
the middle decks \(O(t_U)\) are pairwise disjoint.  Let \(B\) be a bank
of repaired twelve-top **source** packets whose tops and middle decks
are pairwise disjoint.  Write

\[
 S=U(B),\qquad Z=O(B),\qquad |Z|=d|S|.
\tag{0.3}
\]

The conclusions are exact.

1. There is an owner map

   \[
      \omega_T:\operatorname{mid}(T)\longrightarrow\mathcal U,
      \qquad X\in O(t_{\omega_T(X)}),
   \tag{0.4}
   \]

   and the precise additional row quarantine forced by a fixed bank is

   \[
      Q_T(B)=
      \{\omega_T(X):X\in Z\cap\operatorname{mid}(T),
                         \ \omega_T(X)\notin S\}.
   \tag{0.5}
   \]

   If old rows are only deleted, never rerouted, then

   \[
      \boxed{\text{minimum extra leave}=|Q_T(B)|.}
   \tag{0.6}
   \]

2. In particular, replacement on the bank tops has zero quarantine if
   and only if

   \[
   \boxed{
      O(B)\cap
      \operatorname{mid}\bigl(T\setminus T[U(B)]\bigr)
      =\varnothing.}
   \tag{0.7}
   \]

   This is exactly the condition in the prompt; it is not merely
   sufficient.

3. Put

   \[
      e_T(B)=
      \left|Z\cap
      \operatorname{mid}\bigl(T\setminus T[S]\bigr)\right|.
   \tag{0.8}
   \]

   Then

   \[
      \boxed{
      \left\lceil {e_T(B)\over d}\right\rceil
      \le |Q_T(B)|\le e_T(B)\le d|S|.}
   \tag{0.9}
   \]

   For one twelve-top packet for every \(c\in[n]\),
   \(|S|=12n\), so the old \(O(m^2)\)-row bound is the literal estimate

   \[
                        |Q_T(B)|\le12nd=O(m^2).
   \tag{0.10}
   \]

   Equation (0.5), rather than \(12nd\), is its exact value.

4. Adaptive zero-quarantine allocation is an exact **closed decorated
   packet** problem.  A family of literal packet candidates is
   installable with zero quarantine precisely when it is top-disjoint,
   owner-disjoint, and every currently owned middle set which it uses
   is owned by one of its own selected tops.  Section 3 gives a binary
   system which is necessary and sufficient.  A selected solution
   itself installs one physical word per selected top; no quotient
   state or abstract direction is substituted.

5. Ordinary matching sees no obstruction.  Let

   \[
      a=\binom MH,\qquad b=\binom mH,\qquad
      \lambda={a\over b}={W\over N}.
   \tag{0.11}
   \]

   If \(\lambda>d\), \(s=|S|\), and

   \[
      a\ge {ds\lambda\over\lambda-d},
   \tag{0.12}
   \]

   then **every** prescribed squarefree assignment of the \(ds\) bank
   owners to the \(s\) bank tops extends to an atom-level assignment of
   \(d\) distinct contained owners to every other top, with no owner
   repeated.  Thus atom-level alternating paths remove all quarantine.
   In the Gaussian regime and for \(s=m^{O(1)}\), (0.12) holds with
   enormous room.

6. The atom extension is not a physical installation theorem.  The
   family of legal length-\(d\) tight-window decks on one top is not the
   set of bases of a matroid.  More sharply, there is a one-top residual
   owner reservoir of exactly \(d\) contained owners which has scalar
   capacity \(d\) but contains no literal row.  Its unavoidable physical
   leave is one.  Hence neither Hall, matroid intersection, nor ordinary
   alternating paths can prove zero quarantine without a new
   consecutive-window augmenting theorem.

7. Allowing arbitrary literal rerouting gives an exact physical leave
   parameter.  For every auxiliary changed-top set
   \(A\supseteq Q_T(B)\), Section 5 defines a free-owner reservoir
   \(F_B(A)\) and its literal row-packing rank \(r_B(A)\).  The minimum
   possible final row leave is

   \[
      \boxed{
      \ell_T(B)=\min_{A\supseteq Q_T(B)}
                    \bigl(|A|-r_B(A)\bigr).}
   \tag{0.13}
   \]

   Consequently zero quarantine after arbitrary augmenting reroutes is
   equivalent to \(r_B(A)=|A|\) for some \(A\supseteq Q_T(B)\).  This is
   a literal one-path-per-top statement.

8. Coefficient one and protected traces are separate conditions.  If
   \(\Theta(t)\) is the additive vector of all protected nonmiddle traces
   and rooted position--label cells, then a no-reroute zero-quarantine
   installation preserves the old aggregate trace exactly if and only if

   \[
      \sum_{p\in B^-}\Theta(p)=\sum_{U\in S}\Theta(t_U).
   \tag{0.14}
   \]

   The physical rank formula has the analogous balance equation in
   Section 5.  Once installed, every repaired twelve-top firing preserves
   \(\Theta\) and the complete middle-owner vector coefficientwise.

Thus the \(O(m^2)\) quarantine can be replaced by an exact, often much
smaller, owner-closure leave.  It cannot be promoted to a universal
zero by owner Hall theory: Hall is already zero-leave, while literal
tight-window bundling is nonmatroidal and can force a leave even in a
one-top residual instance.  The exact missing theorem is saturation of
the physical rank in (0.13), together with the trace balance when the
master-order ledger is fixed.

## 1. The owner map and exact fixed-bank quarantine

For \(A\subseteq\mathcal U\), write

\[
 T[A]=\{t_U:U\in A\},\qquad
 O_T(A)=\dot\bigcup_{U\in A}O(t_U).
\tag{1.1}
\]

The union is disjoint because \(T\) is coefficient one.  Put

\[
 \mathcal H_T=\mathcal X\setminus\operatorname{mid}(T),
 \qquad h_0=|\mathcal H_T|=W-dN.
\tag{1.2}
\]

Every covered owner has the unique owner top (0.4).

### Theorem 1.1 (literal fixed-bank installation and exact leave)

Let \(Q=Q_T(B)\).  Then

\[
 T_B^0=
 \bigl(T\setminus T[S\cup Q]\bigr)\ \dot\cup\ B^-
\tag{1.3}
\]

is a coefficient-one table of literal retained paths.  It has one row
on every top outside (Q), and its middle hole count is exactly

\[
                         h_0+d|Q|.
\tag{1.4}
\]

Moreover, among all tables obtained by deleting old rows of \(T\) and
inserting (B^-), with no alternative row allowed on a nonbank top,
(|Q|) is the minimum extra row leave.

#### Proof

The bank is internally top-disjoint and owner-disjoint.  If an old row
(t_V), (V\notin S\cup Q), met (Z) in an owner (X), then (X)
would be covered in \(T\), \(\omega_T(X)=V\notin S\), and hence
\(V\in Q\), a contradiction.  Thus every surviving old row is
owner-disjoint from the bank.  The old surviving rows are mutually
owner-disjoint, proving coefficient one in (1.3).

There are \(N-|Q|\) rows in (1.3), each with exactly \(d\) distinct
owners, so it covers (d(N-|Q|)) owners.  This gives (1.4).

For minimality, let (V\in Q).  By definition there is an
(X\in Z\cap O(t_V)).  Keeping (t_V) together with (B^-) gives
coefficient two at (X).  Hence every deletion-only installation must
delete every row indexed by (Q).  Equation (1.3) shows that these
deletions suffice.  \(\square\)

### Corollary 1.2 (the prompt's condition)

Replacing only the rows on \(S=U(B)\) gives a full coefficient-one
table if and only if (0.7) holds.

#### Proof

Condition (0.7) says exactly that \(Q_T(B)=\varnothing\).  Apply
Theorem 1.1 and its minimality statement.  \(\square\)

This proves both directions of the claimed source-installation test.
No average owner load or expected collision estimate is involved.

## 2. Occurrence collisions versus row quarantine

For (V\in Q), define

\[
 q_V=|Z\cap O(t_V)|.
\tag{2.1}
\]

Then \(1\le q_V\le d\), and coefficient one of \(T\) gives the disjoint
sum

\[
                         e_T(B)=\sum_{V\in Q}q_V.
\tag{2.2}
\]

Therefore

\[
                    |Q|\le e_T(B)\le d|Q|,
\tag{2.3}
\]

which is (0.9).  The last inequality in (0.9) follows from
(|Z|=d|S|).

This separates two quantities which the coarse quarantine argument
conflates.  An external row is paid once even if it contains several
bank owners.  Thus (d|S|) is only a worst-case witness count.  The
exact charge is the number of distinct owner tops in (0.5).

There is also an exact mass identity.  Put

\[
 h_B=|Z\cap\mathcal H_T|,
 \qquad
 i_B=|Z\cap O_T(S)|.
\tag{2.4}
\]

Then

\[
                         ds=h_B+i_B+e_T(B),
 \qquad s=|S|.
\tag{2.5}
\]

Hence zero quarantine says that every bank owner is either an old global
hole or is already owned on a bank top.  If it holds, exactly (h_B)
old owner slots on bank tops are released and not reused, balancing the
(h_B) old holes consumed by the bank.

## 3. Exact owner-aware closed packet allocation

Let \(\mathcal C\) be a finite request set; for the broad seed bank one
may take \(\mathcal C=[n]\), where request \(c\) asks for a source row
having \(c\) in rooted position three.  For each \(c\in\mathcal C\),
let \(\mathscr P_c\) be a catalogue of **fully decorated literal repaired
twelve-top sources** satisfying that request.  A candidate \(P\) comes
with its actual twelve tops \(U(P)\), its twelve actual words \(P^-\),
and its squarefree actual owner set \(O(P)\) of size \(12d\).

Candidates are indexed by their request, so write \(z_P\in\{0,1\}\).
Introduce \(y_U\in\{0,1\}\) for every top.  Consider the system

\[
 \sum_{P\in\mathscr P_c}z_P=1
                    \qquad(c\in\mathcal C),
\tag{3.1}
\]

\[
 \sum_{P:U\in U(P)}z_P=y_U\le1
                    \qquad(U\in\mathcal U),
\tag{3.2}
\]

\[
 \sum_{P:X\in O(P)}z_P\le1
                    \qquad(X\in\mathcal X),
\tag{3.3}
\]

and, for every \(P\) and every
\(X\in O(P)\cap\operatorname{mid}(T)\),

\[
                         z_P\le y_{\omega_T(X)}.
\tag{3.4}
\]

Equation (3.4) is the owner-closure implication.  It says that if a
selected packet uses an owner currently carried by \(t_V\), then the
top \(V\) must itself occur in the selected packet bank, so its old row
will be removed.

### Theorem 3.1 (closed decorated source theorem)

The binary system (3.1)--(3.4) has a solution if and only if there is a
literal bank meeting every request which can be installed in \(T\) with
zero row quarantine and with coefficient one.

If, in addition, \(\Theta(t)\) denotes any fixed additive protected-trace
vector, then the installation preserves the complete aggregate
\(\Theta\)-ledger if and only if the solution also satisfies

\[
 \sum_Pz_P\sum_{p\in P^-}\Theta(p)
   =\sum_Uy_U\Theta(t_U).
\tag{3.5}
\]

After installation, every sequence of switches of selected packets
preserves coefficient one and the same \(\Theta\)-ledger.

#### Proof

Given a binary solution, (3.1) supplies every request, (3.2) makes the
candidate tops disjoint, and (3.3) makes their physical middle decks
disjoint.  Let \(B\) be the selected bank and \(S=U(B)\).  If
\(X\in O(B)\cap\operatorname{mid}(T)\), it lies in some selected
candidate \(P\); (3.4) gives \(y_{\omega_T(X)}=1\), hence
\(\omega_T(X)\in S\) by (3.2).  Thus (0.7) holds.  Corollary 1.2
installs the literal source rows with zero quarantine.

Conversely, an installable requested bank defines \(z_P=1\) on its
candidates and \(y_U=1\) on its top union.  Request coverage, top
disjointness and owner disjointness give (3.1)--(3.3), while (0.7) gives
(3.4).

Only the rows on \(S\) change during installation, so equality of the
old and new aggregate protected ledgers is exactly (3.5).  The repaired
twelve-top theorem says, packet by packet, that source and target shores
have the same squarefree middle support and the same protected trace
vector.  Therefore every later firing preserves both ledgers.  \(\square\)

This is a closure problem, not an ordinary matching problem.  Constraint
(3.4) can force a candidate to select tops belonging to other candidates;
finite closed directed circuits are allowed and, when external owners
are used, necessary.  Top/owner matching alone omits precisely these
implications.

## 4. Hall and augmenting paths solve the unbundled problem

Erase the requirement that the \(d\) owners assigned to one top form a
consecutive-window deck.  Join \(U\in\mathcal U\) to \(X\in\mathcal X\)
when \(X\subset U\).  Its left and right degrees are

\[
                         a=\binom MH,
 \qquad                   b=\binom mH,
\tag{4.1}
\]

and \(a/b=\lambda=W/N\).

### Theorem 4.1 (robust forced-owner extension)

Let \(S\subseteq\mathcal U\), \(|S|=s\), and suppose that each
\(U\in S\) has already been assigned \(d\) distinct contained owners,
with all \(ds\) assigned owners distinct.  If \(\lambda>d\) and (0.12)
holds, this forced assignment extends to an assignment of \(d\) distinct
contained owners to every top in \(\mathcal U\), with no owner used
twice.

#### Proof

Let \(Z\) be the set of forced owners.  Clone every top outside \(S\)
into \(d\) left vertices and delete \(Z\) on the right.  It suffices to
verify Hall.

For a nonempty set \(A\subseteq\mathcal U\setminus S\), let
\(\Gamma(A)\) be its owner neighbourhood before \(Z\) is deleted.
Counting incidences gives

\[
 a|A|\le b|\Gamma(A)|,
 \qquad |\Gamma(A)|\ge\lambda|A|.
\tag{4.2}
\]

Also \(|\Gamma(A)|\ge a\), because \(A\) contains at least one top.
Consequently

\[
 |\Gamma(A)\setminus Z|
 \ge\max\{a,\lambda|A|\}-ds.
\tag{4.3}
\]

If

\[
                         |A|\ge{ds\over\lambda-d},
\tag{4.4}
\]

then the second term in (4.3) is at least \(d|A|\).  If (4.4) fails,
(0.12) gives

\[
 a-ds\ge {d^2s\over\lambda-d}>d|A|.
\tag{4.5}
\]

Thus every clone set satisfies Hall's inequality.  An integral matching
saturates all remaining clones and extends the forced assignment.
\(\square\)

At \(H=(1+o(1))\sqrt{m\log m}\),

\[
 \log a=\Theta\!\left(H\log{m\over H}\right),
\tag{4.6}
\]

whereas the right side of (0.12) is polynomial whenever
\(s=m^{O(1)}\).  Thus (0.12) holds with superpolynomial room for the
broad twelve-top bank.

If one starts from the atom assignment underlying \(T\), split each
top into \(d\) clones.  The old matching and the matching from Theorem
4.1 have a symmetric difference consisting of alternating cycles and
alternating paths whose endpoints are old and new owner holes.  Hence
ordinary augmenting paths genuinely give a zero-leave **owner-atom**
reallocation.

The qualification is essential: an intermediate or final group of
\(d\) matched owner atoms at one top need not be the deck of any word.

## 5. Exact physical augmenting rank

Return to literal rows.  Fix the bank \(B\), and put \(Q=Q_T(B)\).
For every \(A\subseteq\mathcal U\setminus S\) with \(Q\subseteq A\),
define

\[
 F_B(A)=
 \bigl(\mathcal H_T\ \dot\cup\ O_T(S\cup A)\bigr)\setminus Z.
\tag{5.1}
\]

Since \(A\supseteq Q\), every member of \(Z\) lies either in
\(\mathcal H_T\) or in \(O_T(S\cup A)\).  Therefore

\[
                         |F_B(A)|=h_0+d|A|.
\tag{5.2}
\]

A family \(\mathcal R\) is an \(A\)-**physical augmentation** if

1. every member is one literal rooted length-\(d\) tight-window row on
   a top in \(A\);
2. no two members use the same top;
3. their middle decks are pairwise disjoint; and
4. every one of their middle owners belongs to \(F_B(A)\).

Let

\[
 r_B(A)=\max\{|\mathcal R|:\mathcal R
                    \text{ is an }A\text{-physical augmentation}\}.
\tag{5.3}
\]

This is a rank of actual path configurations, not a rank of arbitrary
owner subsets.

### Theorem 5.1 (exact minimum physical leave)

Among all coefficient-one partial tables which contain the complete
literal source bank \(B^-\) and which may otherwise change arbitrary
rows of \(T\), the minimum row deficit is exactly

\[
                         \ell_T(B)
 =\min_{\substack{A\subseteq\mathcal U\setminus S\\Q\subseteq A}}
       \bigl(|A|-r_B(A)\bigr).
\tag{5.4}
\]

In particular, a full coefficient-one physical installation exists if
and only if

\[
                 r_B(A)=|A|
 \quad\text{for some }A\supseteq Q.
\tag{5.5}
\]

#### Proof

Fix \(A\supseteq Q\), remove the old rows on \(S\cup A\), insert
\(B^-\), and choose an \(A\)-physical augmentation of maximum size.
All unchanged rows outside \(S\cup A\) remain mutually disjoint.  Their
used owner set is

\[
             \operatorname{mid}(T)\setminus O_T(S\cup A).
\tag{5.6}
\]

The complement of (5.6) after the bank owners \(Z\) are occupied is
exactly \(F_B(A)\).  Conditions 3--4 therefore make the augmentation
owner-disjoint from the bank, from the unchanged rows, and internally.
It installs \(r_B(A)\) rows on the \(|A|\) available nonbank tops, so
the leave is \(|A|-r_B(A)\).  This proves the upper bound in (5.4).

Conversely, let \(T'\) be any coefficient-one partial table containing
\(B^-\).  Let \(A\) be the nonbank tops on which \(T'\) does not retain
the old row \(t_U\), including every omitted top.  Every \(V\in Q\)
belongs to \(A\), because its old row collides with \(Z\).  Each new
nonbank row of \(T'\) is disjoint from \(Z\) and from every unchanged
old row, so its deck lies in \(F_B(A)\).  These new rows form an
\(A\)-physical augmentation.  If the final leave is \(\ell\), there are
\(|A|-\ell\) such rows.  Hence

\[
             |A|-\ell\le r_B(A),
 \qquad       \ell\ge |A|-r_B(A)\ge\ell_T(B).
\tag{5.7}
\]

This proves equality and (5.5).  \(\square\)

### Trace-faithful version

For an \(A\)-augmentation \(\mathcal R\), the resulting table has the
same complete protected trace vector as \(T\) if and only if

\[
 \boxed{
 \sum_{p\in B^-}\Theta(p)+\sum_{r\in\mathcal R}\Theta(r)
   =\sum_{U\in S\cup A}\Theta(t_U).}
\tag{5.8}
\]

Indeed all rows outside \(S\cup A\) cancel from the comparison.  If
\(r_B^\Theta(A)\) denotes the maximum size of an \(A\)-physical
augmentation satisfying (5.8), then the trace-faithful minimum leave is

\[
 \ell_T^\Theta(B)=
 \min_{A\supseteq Q}\bigl(|A|-r_B^\Theta(A)\bigr),
\tag{5.9}
\]

with the minimum restricted to \(A\) for which (5.8) is feasible.
Thus owner closure and trace balance are both literal and separately
visible.

## 6. Tight-window decks are nonmatroidal

Assume \(H\ge3\) and \(d\ge2H+3\).  On a fixed top \(U\), let

\[
 w=(w_1,\ldots,w_{d+H-1})
\tag{6.1}
\]

be injective and define

\[
 J_j(w)=\{w_j,\ldots,w_{j+H-1}\},
 \qquad
 X_j=U\setminus J_j(w),
 \qquad 1\le j\le d.
\tag{6.2}
\]

Then

\[
                         D=\{X_1,\ldots,X_d\}
\tag{6.3}
\]

is a literal retained middle deck.  Choose an interior index

\[
                         H+2\le i\le d-H-1.
\tag{6.4}
\]

The one-window chronology theorem in
`MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md`
says that no other literal deck can differ from \(D\) by removing only
the interior owner \(X_i\) and inserting one new owner.

### Theorem 6.1 (basis exchange fails)

The family of literal length-\(d\) tight-window decks on \(U\), regarded
as \(d\)-subsets of \(\binom Um\), is not the family of bases of a
matroid.

#### Proof

Choose a second injective word whose retained \(H\)-windows avoid the
particular set \(J_i(w)\); for example, place two elements of \(J_i(w)\)
at word positions whose distance is at least \(H\).  Let \(D'\) be its
literal deck.  Then \(X_i\notin D'\).

If the deck family were the bases of a matroid, basis exchange applied
to \(D,D'\) and \(X_i\in D\setminus D'\) would give some
\(Y\in D'\setminus D\) for which

\[
                         D-X_i+Y
\tag{6.5}
\]

is a literal deck.  But (6.5) differs from \(D\) in exactly one owner
and removes the interior phase \(i\), contrary to the one-window
chronology theorem.  \(\square\)

### Corollary 6.2 (one unavoidable physical row leave)

Choose any \(Y\in D'\setminus D\) and put

\[
                         F=(D\setminus\{X_i\})\cup\{Y\}.
\tag{6.6}
\]

Then \(F\) consists of exactly \(d\) distinct rank-\(m\) owners contained
in \(U\), but no literal retained row on \(U\) has its deck contained in
\(F\).

#### Proof

Any literal row deck has size \(d\).  If it were contained in the
\(d\)-set \(F\), it would equal \(F\).  This is forbidden by the same
interior one-window chronology theorem.  \(\square\)

Thus the residual instance with sole unfilled top \(U\) and free owner
reservoir \(F\) has an atom matching saturating the top and physical
rank zero.  Its minimum literal leave is one.  This example does not
claim that every \(F_B(A)\) arising from a full table has this form.  It
proves the decisive logical boundary: zero physical leave is not a
consequence of owner capacity, Hall inequalities, or a matroid
augmentation theorem.  Special structure of the actual residual
reservoir must be used.

## 7. Consequences for the twelve-top source bank

The owner-aware status is now exact.

### Proved

1. For a fixed literal bank, (0.5) is the exact set of additionally
   conflicting rows, and (0.6) is the exact deletion-only leave.
2. The zero-quarantine criterion is precisely (0.7).
3. Adaptive zero-quarantine bank selection is exactly the closed
   decorated packet system (3.1)--(3.4), with (3.5) when the old
   nonmiddle ledger must be preserved.
4. Every polynomial-size forced bank extends with zero leave after the
   consecutive-window bundling is erased.
5. Arbitrary literal rerouting has the exact minimum-leave formula
   (5.4), and the trace-faithful version is (5.9).
6. The literal deck family is nonmatroidal, and a one-top residual
   instance can have atom deficiency zero but physical deficiency one.
7. Once a source bank is installed, repaired packet firings preserve
   the complete owner and protected-trace vectors at every step.

### Not proved

1. A solution of the closed decorated packet system for an arbitrary
   prescribed full table \(T\).
2. Saturation \(r_B(A)=|A|\) for some augmenting set \(A\).
3. The trace-balanced saturation required by (5.8).
4. A chronological decomposition of such a saturation into bounded
   repaired macros.

Therefore the old \(O(m^2)\) quarantine estimate has been sharpened to
an exact physical leave and an exact zero criterion.  A universal
zero-quarantine theorem would be a new consecutive-window augmenting
factor theorem; it is not hidden inside ordinary matching or matroid
intersection.
