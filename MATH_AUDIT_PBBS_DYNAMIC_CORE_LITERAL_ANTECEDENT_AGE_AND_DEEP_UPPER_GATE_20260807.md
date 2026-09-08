# Dynamic cores do not by themselves lift a Hamilton owner path to one literal antecedent

**Date:** 2026-08-07  
**Status:** exact sliding-OR and pinned-collar characterization, exact
run-age transition, and exact deep-upper rigidity statement.  The abstract
equal-or-adjacent core lift is correct, but an arbitrary Hamilton owner
path need not have any width-\(d+2\) source antecedent.  Core changes also
require anticipatory source erosion, not merely a same-edge core update.

## 1. Verdict

Put

\[
 L=d+2.
\tag{1.1}
\]

Three distinct layers must not be conflated:

1. an abstract rank-\(m\) Johnson owner path \((T_i)\);
2. a decomposition \(T_i=G_i\mathbin{\dot\cup}Q_i\) with
   \(|G_i|=m-L\) and equal-or-adjacent cores; and
3. nonempty source letters \((A_j)\) satisfying

   \[
   T_i=\bigcup_{j=i}^{i+L-1}A_j.
   \tag{1.2}
   \]

The dynamic-core tracking theorem proves layer 2 from layer 1.  It does
not prove layer 3.  The obstruction is already visible in one coordinate:
every source occurrence creates an owner-membership run of \(L\)
consecutive windows, so an owner coordinate cannot appear in a positive
run shorter than \(L\).

Even after a source exists, a prescribed clean collar fixes individual
source letters, not only their \(L\)-window unions.  Its compatibility is
an \(L\)-step boundary-state condition.  Finally, all intervals longer
than \(L\) are rigid unions of consecutive owners, so changing the core
decomposition cannot repair a deficient deeper-upper deck.

## 2. Exact sliding-OR criterion

First work cyclically; the opened-path version is identical away from the
two ends and carries the last \(L-1\) source letters as boundary state.
Let \(T_i\subseteq[n]\) be prescribed owner sets indexed by
\(\mathbb Z_N\).

For a coordinate \(c\), write

\[
 b_i(c)=\mathbf 1_{\{c\in T_i\}}.
\tag{2.1}
\]

A source occurrence \(c\in A_j\) contributes \(c\) precisely to the
\(L\) owner starts

\[
 j-L+1,\ldots,j.
\tag{2.2}
\]

Define the safe source set

\[
 K_j=\bigcap_{r=j-L+1}^{j}T_r.
\tag{2.3}
\]

Thus \(c\) may occur at source position \(j\) without changing the
prescribed owner row if and only if \(c\in K_j\).

### Theorem 2.1 (un-pinned antecedent criterion)

There is a cyclic word of nonempty source letters satisfying (1.2) if and
only if:

1. every maximal positive run of every binary word \(b(c)\) has length at
   least \(L\); and
2. \(K_j\ne\varnothing\) at every source position \(j\).

When these conditions hold, the maximal canonical antecedent

\[
 \boxed{A_j=K_j}
\tag{2.4}
\]

works.

#### Proof

Necessity of condition 2 follows from

\[
 A_j\subseteq T_{j-L+1}\cap\cdots\cap T_j=K_j.
\tag{2.5}
\]

If \(c\in A_j\), (2.2) gives a positive owner run of length \(L\)
containing all those starts.  Hence every positive owner occurrence must
belong to a positive run of length at least \(L\), proving condition 1.

Conversely, let \(c\in T_i\).  Its positive run has length at least
\(L\), so there is an \(L\)-subinterval of that run containing \(i\).
Let \(j\) be its right endpoint.  Then

\[
 i\in[j-L+1,j],\qquad c\in K_j=A_j.
\tag{2.6}
\]

Thus the right side of (1.2) contains every element of \(T_i\).
Equation (2.5) gives the reverse containment.  Condition 2 makes every
\(A_j\) nonempty.  \(\square\)

For a Johnson path in the intended range, condition 2 is usually
automatic: among \(L\) consecutive owners at most \(L-1\) elements of
the first owner can be deleted, so

\[
 |K_j|\ge m-(L-1)>0.
\tag{2.7}
\]

The positive-run condition is not automatic.  For example, if
\(|B|=m-1\) and \(a,c,e\notin B\) are distinct, then

\[
 B\cup\{a\},\quad B\cup\{c\},\quad B\cup\{e\}
\tag{2.8}
\]

is a valid simple Johnson path, but \(c\) has a positive run of length
one.  No width-\(L\) antecedent exists for this path when \(L\ge2\), even
though the abstract dynamic-core theorem supplies a core lift.

## 3. Exact pinned-collar criterion

Let \(D\) be a set of source positions at which exact nonempty letters
\(P_j\) are prescribed, as happens inside isolated clean collars.  For
each coordinate \(c\), put

\[
 F_c^1=\{j\in D:c\in P_j\},
\qquad
 F_c^0=\{j\in D:c\notin P_j\},
\tag{3.1}
\]

and define its safe emission positions

\[
 E_c=\{j:c\in K_j\}
 =\{j:b_{j-L+1}(c)=\cdots=b_j(c)=1\}.
\tag{3.2}
\]

### Theorem 3.1 (pinned erosion criterion)

There is a nonempty source word satisfying (1.2) and
\(A_j=P_j\) for every \(j\in D\) if and only if:

1. \(F_c^1\subseteq E_c\) for every coordinate \(c\);
2. for every \(i\) with \(c\in T_i\),

   \[
   [i,i+L-1]\cap(E_c\setminus F_c^0)\ne\varnothing;
   \tag{3.3}
   \]

3. \(K_j\ne\varnothing\) at every unpinned position \(j\notin D\).

#### Proof

A forced occurrence must be safe, giving condition 1.  Every positive
owner bit at \(i\) must be covered by some source position
\(j\in[i,i+L-1]\).  That position must be safe and cannot be pinned to
zero, giving condition 2.  Every unpinned source letter must contain some
safe coordinate, giving condition 3.

Conversely, at a pinned position use \(P_j\).  At every unpinned position
put

\[
 A_j=K_j.
\tag{3.4}
\]

All chosen occurrences are safe.  Conditions 1--2 show that every
positive owner bit is covered, and no zero owner bit can be introduced.
Condition 3 gives nonempty letters.  Hence (1.2) holds.  \(\square\)

This theorem identifies the exact halo of a collar.  Prescribing one
source position \(j\) tests the owner bits on starts
\(j-L+1,\ldots,j\); covering owner start \(i\) tests source positions
\(i,\ldots,i+L-1\).  Therefore a clean collar's three central owners are
not enough to certify insertion into an arbitrary Hamilton path.  The
owner chronology and source pins must agree throughout its \(L-1\)-step
incoming and outgoing halo.

Separated collar supports remove pin--pin conflicts, but they do not
remove these halo tests against the intervening owner path.

## 4. Signed run-age transition

PBBS residence asks for both positive and negative owner runs to have the
required floor.  For every coordinate, record its current sign
\(\epsilon_i(c)=\mathbf1_{\{c\in T_i\}}\) and its capped run age

\[
 \alpha_i(c)=
 \min\{L,\text{length of the current constant run ending at }i\}.
\tag{4.1}
\]

Suppose

\[
 T_{i+1}=T_i-x_i+y_i.
\tag{4.2}
\]

The exact residence-legal transition is:

\[
 \begin{array}{c|c|c}
 \text{coordinate}&(\epsilon_i,\alpha_i)&
                   (\epsilon_{i+1},\alpha_{i+1})\\ \hline
 x_i&(1,L)&(0,1)\\
 y_i&(0,L)&(1,1)\\
 c\notin\{x_i,y_i\}&(\epsilon,\alpha)&
              (\epsilon,\min\{L,\alpha+1\}).
 \end{array}
\tag{4.3}
\]

On a closed chronology, every constant run has length at least \(L\) if
and only if every sign-changing transition obeys (4.3) and the terminal
age state matches the initial state.

The fixed-core rail and the punctured core-swap splice realize this table
by imposing \(2L\)-spacing on toggle occurrences.  An arbitrary
middle-levels Hamilton cycle does not come with (4.3).  Good-turn
abundance and equal-or-adjacent core tracking do not constrain these ages.

For existence of some source antecedent, only the positive-run half of
(4.3) is forced by Theorem 2.1.  The negative-run half is the additional
PBBS biresidence requirement.  Exact collar pins then impose the stronger
criterion of Theorem 3.1.

## 5. Why a same-edge core update is not a literal splice

There is a local source obstruction hidden by the abstract decomposition.
Suppose the owner transition (4.2) deletes \(x_i\).  From

\[
 T_i=\bigcup_{j=i}^{i+L-1}A_j,\qquad
 T_{i+1}=\bigcup_{j=i+1}^{i+L}A_j,
\tag{5.1}
\]

one obtains the forced endpoint pattern

\[
 \boxed{
 x_i\in A_i,\qquad
 x_i\notin A_{i+1}\cup\cdots\cup A_{i+L},}
\tag{5.2}
\]

and, dually,

\[
 \boxed{
 y_i\notin A_i\cup\cdots\cup A_{i+L-1},\qquad
 y_i\in A_{i+L}.}
\tag{5.3}
\]

Indeed, the shared \(L-1\) source positions belong to both owner windows.
An element deleted from the second union can occur only at the departing
position \(A_i\), and an element newly entering can occur only at
\(A_{i+L}\).

Now consider the second row of the abstract dynamic-core recurrence:

\[
 x_i\in G_i,\qquad
 G_{i+1}=G_i-x_i+w_i.
\tag{5.4}
\]

If the old rail literally writes every core element into its ordinary
source letters, then \(x_i\) occurs throughout
\(A_{i+1},\ldots,A_{i+L-1}\), contradicting (5.2).  Hence a core element
cannot be removed from the owner and from the literal core description on
the same edge without preparation.  Its copies must be punctured from the
next \(L-1\) source positions before the owner departure becomes visible.

This is an anticipatory erosion constraint: the core trajectory alone is
not a Markov state for literal source concatenation.  One must also carry
the ordered last \(L-1\) source letters, or an equivalent per-coordinate
erosion/age state.

The audited punctured core-swap template is a genuine local adapter because
it performs exactly such preparation.  It first demotes the departing
core coordinate to a queue toggle while keeping the owner set valid, and
only on the following owner step lets that coordinate leave.  Under
\(2L\)-spacing it also satisfies (4.3).  However:

1. its support has \(L+1\) prescribed source positions;
2. positive-density overlapping adapters still require literal
   prescription consistency;
3. it exports one authoritative forced-coatom/compiler ticket; and
4. it does not turn the arbitrary same-edge recurrence (5.4) into a
   source-local transition rule.

Thus the local core-swap theorem is useful, but it is not a global lift of
the abstract dynamic-core path.

## 6. Deeper-upper rigidity

Once the owner path is fixed, every source antecedent has the same upper
interval values.  For every \(q\ge0\),

\[
 \boxed{
 \bigcup_{j=i}^{i+L+q-1}A_j
 =\bigcup_{r=0}^{q}T_{i+r}.}
\tag{6.1}
\]

#### Proof

The union of the \(q+1\) consecutive length-\(L\) windows starting at
\(i,\ldots,i+q\) is exactly the source interval from \(i\) through
\(i+L+q-1\).  \(\square\)

Suppose the owner transitions introduce labels
\(y_1,\ldots,y_q\).  Then

\[
 \bigcup_{r=0}^{q}T_{i+r}
 =T_i\cup\{y_1,\ldots,y_q\},
\tag{6.2}
\]

so

\[
 \left|\bigcup_{r=0}^{q}T_{i+r}\right|
 =m+\left|\{y_1,\ldots,y_q\}\setminus T_i\right|.
\tag{6.3}
\]

The desired rank \(m+q\) occurs exactly when all \(q\) entering labels are
distinct and none lies in \(T_i\).  The immediate upper row \(q=1\) is
built into a Johnson edge.  Distinct consecutive upper vertices also
force the correct rank for \(q=2\).  At \(q=3\), owner and immediate-upper
simplicity no longer suffice.

For example, let \(|R|=m-2\) and let \(a,b,c,e\) be distinct outside
\(R\).  The path

\[
 \begin{aligned}
 T_0&=R\cup\{a,b\},\\
 T_1&=R\cup\{b,c\},\\
 T_2&=R\cup\{c,e\},\\
 T_3&=R\cup\{e,a\}
 \end{aligned}
\tag{6.4}
\]

has distinct owners and distinct immediate upper values, but

\[
 |T_0\cup T_1\cup T_2\cup T_3|
 =|R\cup\{a,b,c,e\}|=m+2<m+3.
\tag{6.5}
\]

If the owner chronology satisfies the negative-run part of the
\(L\)-residence rule, then for \(q\le L-1\) no entering coordinate can
have appeared in the previous \(q\) owners.  Hence (6.3) has rank
\(m+q\) throughout that local depth range.  This proves rank legality,
not target coverage or one-copy injectivity.

Equation (6.1) has two consequences:

1. a source or core splice that preserves the owner sequence
   automatically preserves every longer-window upper value; but
2. no choice of source letters or dynamic cores can repair a missing,
   repeated, or rank-deficient deeper-upper target of that owner
   sequence.

Middle-levels Hamiltonicity supplies all owners and the \(q=1\) upper
shore exactly once.  It says nothing comparable for the union maps in
(6.1) at larger \(q\).

## 7. Exact surviving lift

A proof-safe dynamic-core lift must refine the abstract states
\((G_i,Q_i)\) by at least:

1. the signed capped owner-run ages in (4.1);
2. the ordered \(L-1\)-letter source tail, or the equivalent pinned
   erosion state of Theorem 3.1;
3. the scheduled demotions of core coordinates that will leave after the
   required erosion delay;
4. the exact input/output pin states of every isolated clean collar and
   punctured adapter;
5. all exported forced-coatom/compiler tickets; and
6. the global inventory of longer owner unions in (6.1).

The required theorem is therefore:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
Choose an owner/upper Hamilton chronology together with a residence-legal
age trajectory and a source-tail/core trajectory satisfying every collar
pin, such that all longer consecutive-owner unions give the required
deep-upper deck and the short source intervals give the common lower
compiler.
\end{minipage}}
\tag{7.1}
\]

The current dynamic-core theorem proves only the projection onto
\((T_i,G_i,Q_i)\).  The Hamilton-first good-turn theorem proves only the
projection onto sparse owner/immediate-upper packet paths.  Neither
projection implies the joint lift (7.1).

Accordingly, there is no common width-\(d+2\) antecedent theorem yet for
an arbitrary Hamilton owner path with isolated clean collars.  The exact
first obstruction is the run/erosion state; after that is repaired, the
deeper-upper union inventory and the lower compiler remain genuinely
global.
