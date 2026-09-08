# A two-position tight pivot has exact algebraic carry, a sharp residence horizon, and a one-ended extension automaton

Date: 2026-08-01  
Lane: A, tight pivot / one-ended source extension / additive-one owner path  
Status: unconditional local two-position repair, exact inherited algebraic
Pascal carry, sharp finite shared-bank residence horizon, and exact
necessary-and-sufficient extension theorem.  Absolute maximal erosion and
an automatic *fresh enrichment-site* reset are disproved.  Unbounded
recurrence additionally requires a shared-bank residence rebase/rethread.
Existence of the required global owner path, occurrence matching, and
ambient cap state remains open.

## 0. Outcome

Fix depth \(h\ge2\), owner rank \(r\), a base \(B\) of size \(r-h\ge2\), and
distinct \(x_L,x_R\in X\subseteq B\).  The sparse split-pivot source can be
made literally lower- and upper-q1 tight by enlarging only two source
letters:

\[
 \{\lambda_j\}\longmapsto
       (B-\{x_R\})\cup\{\lambda_j\},\qquad 1\le j<h,
\]
\[
 \{\rho_s\}\longmapsto
       (B-\{x_L\})\cup\{\rho_s\},\qquad 2\le s\le h.       \tag{0.1}
\]

The pair \((j,s)\) is the canonical interior menu of size \((h-1)^2\).
Two positions are necessary and sufficient among enrichment-only repairs;
singleton shores have the additional seam choices classified in Theorem
1.2.  This improves the
four-position source in
MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md.

Place the resulting \(4h+1\)-letter source at the initial boundary of a
longer word.  Its exact continuation state is not just its last owner.  It
is

\[
 \boxed{\text{ordered last \(h\) source letters}
        +\text{ capped signed owner-run ages}.}           \tag{0.2}
\]

Iteration of the transition rule in Section 3 is necessary and sufficient
for a prescribed owner continuation to have a literal source continuation,
native lower q1 cells, and residence.  For the pivot prefix, the first
successor owner is forced to replace \(\rho_h\), and its entering coordinate
must avoid one explicit deadline set.

All owner, matching, upper, lower, terminal, and mixed-guard equations admit
an exact frozen-prefix maximal-word test.  It is an iff theorem.  Ordinary
maximal erosion does not preserve the prefix: already its first maximal
letter is the whole first owner rather than the displayed singleton.

The two-position cap state is algebraically closed without a fresh
enrichment-site reset.  On a plateau its logical
locations remain \((j,s)\), with the new core coordinate added to both
letters.  On a deadline jump its locations become \((j+1,s)\); the two
enriched physical letters themselves persist under the exact block
embedding.  Hence no local cap, q1, ray, residence, or Pascal packet equation
forces such a reset.  Moving enrichment instead to the two fresh labels can
destroy the old enriched one-cell targets and is only an optional global
recompilation.  Transport of the rest of the old target sectors remains a
separate ambient-row problem.  This algebraic statement is not an
indefinite residence theorem: jump labels reused in opposite banks acquire
a second positive run, and Section 6 gives the exact finite horizon.

## 1. The minimal two-position literal repair

Write

\[
 B=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,\qquad
 X=X_L\mathbin{\dot\cup}X_R,
\]

where \(X_L,X_R\ne\varnothing\), and choose
\(x_L\in X_L,x_R\in X_R\).  All labels below outside \(B\) are fresh and
mutually disjoint; in particular the ground set has size at least
\(r+3h\).  Start with the sparse source

\[
\begin{array}{l}
 \{d^-_1\},\ldots,\{d^-_{h-2}\},
   (C\cup X_L)\cup\{d^-_{h-1}\},
   (X_R-\{x_R\})\cup\{q^-\},\\
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},
   (C\cup X_L)\cup\{\lambda_h\},\\
 X,\\
 (C\cup X_R)\cup\{\rho_1\},
   \{\rho_2\},\ldots,\{\rho_h\},\\
 (X_L-\{x_L\})\cup\{q^+\},
   (C\cup X_R)\cup\{d^+_1\},
   \{d^+_2\},\ldots,\{d^+_{h-1}\}.
\end{array}                                               \tag{1.1}
\]

Empty singleton lists are omitted.  Choose one \(j\in[1,h-1]\) and one
\(s\in[2,h]\), and make exactly the two replacements (0.1).  Call the
resulting word \(A^{j,s}\).

Put

\[
 B^-=(B-\{x_R\})\cup\{q^-\},\qquad
 B^+=(B-\{x_L\})\cup\{q^+\}.                              \tag{1.2}
\]

Its depth-\(h\) owner row is

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1},  \tag{1.3}
\]

where

\[
\begin{aligned}
 L_t&=B^-\cup\lambda[1,t+1]\cup D^-[t+1,h-1],\\
 M_u&=B\cup\rho[1,u]\cup\lambda[u+1,h],\\
 R_t&=B^+\cup\rho[t+1,h]\cup D^+[1,t].
                                                               \tag{1.4}
\end{aligned}
\]

### Theorem 1.1 (two-position q1-tightness)

The enrichment (0.1) changes none of the following:

1. the owner row (1.3);
2. the pre-insertion row
   \[
        L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},
        R_0,\ldots,R_{h-1},
   \]
   where \(U_u=M_u\cup M_{u+1}\) has rank \(r+1\);
3. the pivot rays
   \[
       X,\quad B\cup\lambda[h-i+1,h],\quad
       B\cup\rho[1,i]\qquad(1\le i<h);
   \]
4. the owner residence traces, support \(r+3h\), source length, or
   incidence count.

Every one of the \(3h\) native shared depth-\(h-1\) cells equals the
corresponding owner intersection, and every native depth-\(h+1\) cell
equals the corresponding owner union.  Both literal q1 palettes are
injective.

#### Proof

Every owner window containing \(\lambda_j\) already contains
\(B-\{x_R\}\), and every owner window containing \(\rho_s\) already contains
\(B-\{x_L\}\).  Thus the owner and pre-owner rows do not change.  The two
defective left shared intervals both contain every
\(\lambda_1,\ldots,\lambda_{h-1}\).  Their combined missing set is

\[
        (C\cup X_L)\cup(X_R-\{x_R\})=B-\{x_R\}.           \tag{1.5}
\]

The chosen \(\lambda_j\) therefore closes both left deficits.  The two
right defective shared intervals both contain every
\(\rho_2,\ldots,\rho_h\), and their combined missing set is
\(B-\{x_L\}\); the chosen \(\rho_s\) closes both.

No other shared cell can overshoot its owner intersection: the added set is
contained in every owner using the enriched position.  Upper tightness is
automatic because the union of two adjacent owner windows is the OR of
their spanning \(h+2\) source letters.  The previously proved special-label
signatures separate all five transition classes on both shores.

The inserted \(X\) is still contained in the union of the two adjacent old
letters.  Hence monotone insertion preserves every interval OR of the
*enriched pre-word*, and the insertion-born cells are still precisely the
two rays and the one-letter cell \(X\).  This proves every assertion.
\(\square\)

### Theorem 1.2 (minimality and the complete two-position menu)

Among repairs which only enlarge existing source letters while keeping the
owner row fixed, at least two positions must be changed.  The always
available interior equality choices consist of one position from

\[
       \{\lambda_1,\ldots,\lambda_{h-1}\}
       \quad\text{and one from}\quad
       \{\rho_2,\ldots,\rho_h\},                          \tag{1.6}
\]

and adding at least \(B-\{x_R\}\) and \(B-\{x_L\}\), respectively.  They
give the canonical menu of size \((h-1)^2\).

There are precisely two possible extra endpoint positions.  If
\(|X_R|=1\), the left seam position immediately preceding
\(\lambda_1\) may instead be enlarged to \(B^-\).  If \(|X_L|=1\), the
right seam position immediately following \(\rho_h\) may instead be
enlarged to \(B^+\).  Consequently the complete number of minimum-position
pairs is

\[
 (h-1+{\bf1}_{|X_R|=1})(h-1+{\bf1}_{|X_L|=1}).       \tag{1.6a}
\]

#### Proof

The common support of the two nonempty left deficits is the first set of
(1.6).  When \(X_R-\{x_R\}=\varnothing\), the second deficit is empty, so
only the first deficit must be hit and its support additionally contains
the preceding seam position.  Symmetrically, the common support of the
nonempty right deficits is the second set of (1.6), enlarged by its
following seam position exactly when \(X_L-\{x_L\}=\varnothing\).  The left and right position families are
disjoint.  Thus one position cannot repair both shores.  Formula (1.5) and
its right analogue force the inclusion-minimal additions.  Theorem 1.1
proves the interior choices; the two endpoint substitutions give exactly
\(B^-\) and \(B^+\), so the same owner-cap argument proves the exceptional
choices. \(\square\)

For \(h=2\), the unique *interior* choice is \(j=1,s=2\); all seven owners
and all six shared lower cells replay exactly.  The exceptional seam choice
on either shore exists precisely when that shore of \(X\) is a singleton.

From this point onward, \(K_2(j,s)\) denotes the canonical interior menu
(1.6).  The exceptional seam choices satisfy the same local q1 theorem but
have different exported source addresses and are not used in the recurrence
of Section 6.

The two enriched owner caps are

\[
 H_L(j)=(B-\{x_R\})\cup\{\lambda_j\},\qquad
 H_R(s)=(B-\{x_L\})\cup\{\rho_s\}.                       \tag{1.7}
\]

Relative to the sparse source, every protected row containing the first
position must contain \(H_L(j)\), and every protected row containing the
second must contain \(H_R(s)\).  These are exactly two incremental negative
guards.  They do not remove positive reconstruction conditions or the
baseline sparse-prefix guards.

The enriched source deck need not contain the sparse source deck.  All
transparency claims below compare \(A^{j,s}_{\rm pre}\) with
\(A^{j,s}_{\rm post}\), never the sparse and enriched sources.

## 2. Exact boundary state of the prefix

The prefix has \(4h+1\) source letters and \(3h+1\) owners.  Its ordered last
\(h\) source letters are independent of \(j,s\), even when \(s=h\):

\[
\sigma_0=\bigl(
 (X_L-\{x_L\})\cup\{q^+\},
 (C\cup X_R)\cup\{d^+_1\},
 \{d^+_2\},\ldots,\{d^+_{h-1}\}
\bigr).                                                  \tag{2.1}
\]

Their union is

\[
 S_0=(B-\{x_L\})\cup\{q^+\}\cup D^+,
\qquad R_{h-1}=S_0\cup\{\rho_h\}.                         \tag{2.2}
\]

Use signed residence: every maximal constant run, of either membership bit,
which is wholly internal must have length at least \(h+1\); runs meeting a
global endpoint may clip.

For \(1\le t\le h\), define deadline sets

\[
\begin{aligned}
 P_1&=\{q^+,d^+_1,\ldots,d^+_{h-1}\},\\
 P_t&=\{d^+_{t-1},\ldots,d^+_{h-1}\},
                         &&2\le t\le h,\\
 Z_1&=\{x_L,\rho_1,\ldots,\rho_{h-1}\},\\
 Z_t&=\{\rho_{t-1},\ldots,\rho_{h-1}\},
                         &&2\le t\le h.                 \tag{2.3}
\end{aligned}
\]

### Lemma 2.1 (exact trailing obligations)

For a continuation owner sequence \(V_1,V_2,\ldots\), all terminal
positive runs and zero-gaps inherited from the prefix attain length at
least \(h+1\) iff

\[
                  P_t\subseteq V_t,\qquad
                  Z_t\cap V_t=\varnothing
                  \qquad(1\le t\le h).                   \tag{2.4}
\]

No other prefix coordinate imposes a trailing residence condition.

#### Proof

In the terminal owner trace, \(q^+\) has positive age \(h\), and
\(d^+_u\) has positive age \(h-u\).  Coordinate \(x_L\) has terminal zero
age \(h\), and \(\rho_u\), \(u<h\), has terminal zero age \(h-u\).
Every other terminal signed run already has age at least \(h+1\).
Extending each deficient age to \(h+1\) gives (2.3)--(2.4). \(\square\)

The fixed suffix itself automatically carries \(q^+\) for the first new
owner and \(d^+_u\) for its first \(u+1\) new owners.  The negative
requirements are genuine restrictions on appended letters.

### Corollary 2.2 (forced first port)

The first appended rank-\(r\) owner is source-compatible, Johnson-adjacent
to \(R_{h-1}\), physically lower-q1 tight, and residence-compatible exactly
when it has the form

\[
             V_1=S_0\cup\{y\},\qquad
             y\notin R_{h-1}\cup Z_1.                    \tag{2.5}
\]

Any appended source letter \(E_1\) with

\[
       \{y\}\subseteq E_1\subseteq V_1                 \tag{2.6}
\]

realizes this first owner, subject to its ambient cap.  Its physical lower
colour is exactly \(S_0\).

#### Proof

The first new owner window contains all \(h\) letters in (2.1), so it
contains \(S_0\).  Since \(|S_0|=r-1\), a distinct rank-\(r\) Johnson
successor is \(S_0+y\), with \(y\notin R_{h-1}=S_0+\rho_h\).  Condition
\(y\notin Z_1\) is exactly the first negative deadline; the positive
deadline is contained in \(S_0\).  Formula (2.6) realizes the union.
The exiting source letter contributes outside \(S_0\) only \(\rho_h\),
which is absent from \(V_1\), so the shared cell is tight. \(\square\)

The new coordinate \(y\) begins a positive run of age one and must itself
obey the continuation residence rule.

## 3. Source-compatible residence automaton

The preceding calculation is an instance of an exact finite-state theorem.
Let a current source prefix be

\[
                 A_0,\ldots,A_{N-1},\qquad N\ge h+1,
\]

with terminal owner

\[
                 O=\bigcup_{p=N-h-1}^{N-1}A_p.
\]

Let

\[
 \sigma=(A_{N-h},\ldots,A_{N-1}),\qquad
 S=\bigcup\sigma.                                        \tag{3.1}
\]

For every coordinate \(z\), record its terminal owner bit
\(\varepsilon_z={\bf1}_{z\in O}\) and the age \(a_z\) of its current
constant owner-bit run, capped at \(h+1\).

### Theorem 3.1 (exact one-step and iterated extension)

Given a desired next owner \(U\), there is a nonempty appended source letter
\(E\) producing \(U\), preserving native lower q1, and making a legal
residence transition iff

\[
\begin{aligned}
 &S\subseteq U,\qquad U-S\subseteq E\subseteq U,\qquad E\ne\varnothing,\\
 &E\cap(O-S)=\varnothing,                                  \tag{3.2}\\
 &{\bf1}_{z\in U}\ne\varepsilon_z\Longrightarrow a_z=h+1
       \quad\text{for every }z.
\end{aligned}
\]

With a point cap \(K\) and mandatory subset \(D\), replace the middle
interval in (3.2) by

\[
                  (U-S)\cup D\subseteq E\subseteq K\cap U. \tag{3.3}
\]

After a legal step, shift

\[
       \sigma\longmapsto(\sigma_2,\ldots,\sigma_h,E),      \tag{3.4}
\]

replace \(\varepsilon\) by the bit vector of \(U\), reset a changed age to
one, and increase an unchanged age up to the cap \(h+1\).

Iteration of (3.2)--(3.4) is necessary and sufficient for an owner sequence
to be the literal depth-\(h\) continuation of the fixed prefix, with every
native lower q1 cell equal to the owner intersection and every completed
positive run or zero-gap of length at least \(h+1\).

#### Proof

The next owner is \(S\cup E\), giving the first line.  Consecutive owner
windows share the \(h\) letters whose union is \(S\).  The exact identity

\[
 O\cap U=S\cup\bigl((O-S)\cap E\bigr)                     \tag{3.5}
\]

proves the second line.  A changed owner bit closes the preceding constant
run, so residence is equivalent to its capped age being \(h+1\).  The state
update is literal.  Induction proves necessity and sufficiency. \(\square\)

If the eventual right endpoint may clip, no terminal age condition is
needed.  If it will be internalized, iteration must continue until every
unsaturated terminal age is discharged.

The ordered suffix cannot be replaced by its union: different orders have
different next shifted hulls.  The age vector cannot be omitted: two
prefixes with the same suffix and terminal owner but ages one and \(h+1\)
permit different bit flips.

Equivalently, if successive source occurrences of one coordinate have
distance \(\Delta\), residence permits exactly

\[
                 \Delta\le h+1\quad\text{or}\quad
                 \Delta\ge2h+2.                          \tag{3.6}
\]

The band \(h+2\le\Delta\le2h+1\) creates a zero-gap of length at most \(h\).

## 4. Frozen-prefix relative maximal erosion

Fix a complete proposed continuation, including its owner order and every
selected occurrence-matching edge.  Let \({\cal R}\) be the family of all
exact rows that must hold: owner windows, native lower and upper rows,
selected compiler cells, the terminal surplus cell, and every protected or
mixed exterior guard.  A row \(R\) has target \(S_R\) and source-position
set \(I_R\).  Let \(C_p\) be the point cap and \(D_p\) a mandatory subset at
source position \(p\).  Freeze the prefix positions

\[
                  J=\{0,\ldots,4h\}
\]

to their literal letters \(F_p=A^{j,s}_p\).

For each free position \(p\notin J\), put

\[
 K_p=C_p\cap\bigcap_{\substack{R\in{\cal R}\\p\in I_R}}S_R, \tag{4.1}
\]

and define the relative maximal word

\[
 Q^{\max}_p=
 \begin{cases}
 F_p,&p\in J,\\
 K_p,&p\notin J.
 \end{cases}                                               \tag{4.2}
\]

### Theorem 4.1 (exact frozen-prefix extension criterion)

There is a nonempty source word extending the literal prefix, obeying every
point cap and mandatory subset, and realizing every row in \({\cal R}\)
iff

\[
\begin{aligned}
 &D_p\subseteq F_p\subseteq C_p\cap
       \bigcap_{R:p\in I_R}S_R &&(p\in J),\\
 &D_p\subseteq K_p\ne\varnothing &&(p\notin J),           \tag{4.3}\\
 &S_R=\bigcup_{p\in I_R}Q^{\max}_p &&(R\in{\cal R}).
\end{aligned}
\]

When these conditions hold, \(Q^{\max}\) is the unique
componentwise-largest source among words with the prefix frozen.

#### Proof

Every feasible free letter lies in its point cap and in every target row
using it, hence is contained in \(K_p\).  Fixed letters must satisfy the
first line.  Therefore every feasible source is componentwise contained in
\(Q^{\max}\) off the frozen prefix and equals it on the prefix.  The row
screens ensure that the union of \(Q^{\max}\) on a row cannot exceed its
target.  If its union misses a target coordinate, no smaller feasible word
can restore it.  Conversely, (4.3) states directly that \(Q^{\max}\) is a
nonempty cap-legal source realizing all rows. \(\square\)

For owner rows only, (4.1) is the usual maximal erosion intersection.  For
a mixed row, the theorem is equivalently

\[
 E_R\subseteq S_R,\qquad
 S_R=E_R\cup\bigcup_{p\in I_R\setminus J}K_p,             \tag{4.4}
\]

where \(E_R\) is the OR of its frozen prefix letters.  Thus a frozen
overflow \(E_R\nsubseteq S_R\), an empty screened suffix position, or a
missing positive coordinate in (4.4) is a certificate no continuation can
repair.

If the occurrence matching is not fixed, it must be selected outside
Theorem 4.1 and its chosen cells inserted into \({\cal R}\).  Hall in the
union of several cap states is unsound.  For a fixed feasible maximal word,
the remaining target-to-cell selection is ordinary bipartite matching.

### Corollary 4.2 (absolute maximal erosion does not preserve the prefix)

Even with no continuation, the absolute owner erosion at source position
zero is

\[
                 \bigcap_{i:\,0\in[i,i+h]}T_i=T_0=L_0,
\]

whereas the literal first source letter is

\[
 F_0=\begin{cases}
       \{d^-_1\},&h\ge3,\\
       (C\cup X_L)\cup\{d^-_1\},&h=2.
     \end{cases}
\]

In both cases \(F_0\subsetneq L_0\), since \(L_0\) also contains the fresh
labels \(q^-\) and \(\lambda_1\).  Hence ordinary maximal erosion changes
the prefix.  A universal statement that maximal
erosion of a resident protected owner continuation preserves the literal
prefix is false.  Theorem 4.1 is the sharp screened replacement.

Residence does not imply source compatibility either.  The abstract
Johnson successor

\[
                  R_{h-1}-x_R+y
\]

may legally end the already long \(x_R\)-run, but it omits
\(x_R\in S_0\) and cannot follow the fixed source suffix.  Conversely,
\(S_0+x_L\) is source-compatible but reintroduces \(x_L\) after a zero-gap
of only \(h\) owners.  These are independent one-row obstructions.

## 5. The exact \(K_2\) cap state

The two enriched positions are

\[
 p_L=h+j-1,\qquad p_R=2h+s,                              \tag{5.1}
\]

with mandatory literal letters \(H_L(j),H_R(s)\) from (1.7).  Given every
ambient cap and exact row, define

\[
 \widehat K_p=C_p\cap\bigcap_{R:p\in I_R}S_R.            \tag{5.2}
\]

The chosen menu state is admissible exactly when

\[
 H_L(j)\subseteq\widehat K_{p_L},\qquad
 H_R(s)\subseteq\widehat K_{p_R},                        \tag{5.3}
\]

and every affected row reconstructs with the two prefix letters frozen to
\(H_L(j),H_R(s)\), as in Theorem 4.1.  Equality in (5.3) follows only when
the corresponding one-cell value is itself imposed as an exact row; it is
not a general cap condition.  Equivalently, if
the sparse source already realized a fixed row bank, enrichment preserves
that bank iff every row through \(p_L\) contains \(B-\{x_R\}\), every row
through \(p_R\) contains \(B-\{x_L\}\), and the two point caps contain the
enriched letters.

Thus \(K_4\) reduces to \(K_2\) only for the incremental negative-cap
state.  Mixed-row positive coverage, the ordered suffix (2.1), residence
ages, and all baseline sparse-prefix guards remain exported data.

## 6. The proof-safe no-reset \(K_2\) recurrence

The local recurrence never needs to move enrichment to fresh labels.
For this section, write the literal source in four length-\(h\) blocks as

\[
 A^{j,s}=E_h^-A_h^-(j)[X]A_h^+(s)E_h^+,               \tag{6.0}
\]

where the blocks are, in order, the four displayed lines of (1.1), with
the two enrichments (0.1) made in the middle pair.
The literal ordered right suffix is

\[
 \omega_h:=E_h^+=\bigl(
 (X_L-\{x_L\})+q^+,(C\cup X_R)+d^+_1,
 d^+_2,\ldots,d^+_{h-1}\bigr).                         \tag{6.0a}
\]

On a depth plateau, let the owner rank rise from \(r\) to \(r+1\), keep
depth \(h\), and add the new core coordinate \(\beta\):

\[
 B'=B\cup\{\beta\},\qquad C'=C\cup\{\beta\}.           \tag{6.1}
\]

Keep the menu indices:

\[
                         (j,s)\longmapsto(j,s).          \tag{6.2}
\]

The two enriched letters become

\[
 (B'-\{x_R\})+\lambda_j,qquad
 (B'-\{x_L\})+\rho_s.                                  \tag{6.3}
\]

Thus their values acquire the same mandatory \(\beta\) as every local
owner, pre-row cell, and transported strict ray \(P_i,S_i\); the singleton
ray \(X\) stays untagged.  Their logical source addresses do not move:
\(p'_L=p_L,p'_R=p_R\).

At a deadline jump put \(H=h+1\), keep \(B'=B,C'=C\), and write

\[
 \lambda'=(\alpha,\lambda_1,\ldots,\lambda_h),\qquad
 \rho'=(\rho_1,\ldots,\rho_h,\gamma).                  \tag{6.4}
\]

The inherited block identities are literal:

\[
\begin{aligned}
 E_H^-&=(\{\gamma\})E_h^-,&
 A_H^-(j+1)&=(\{\alpha\})A_h^-(j),\\
 A_H^+(s)&=A_h^+(s)(\{\gamma\}),&
 E_H^+&=E_h^+(\{\alpha\}).                            \tag{6.5}
\end{aligned}
\]

Consequently the proof-safe transition is

\[
                         (j,s)\longmapsto(j+1,s).        \tag{6.6}
\]

The old enriched letters are not thinned, moved, or duplicated: they occur
as the same set-valued source letters inside the two embedded parent
blocks.  At literal global source indices,

\[
                         p'_L=p_L+2,\qquad p'_R=p_R+2.   \tag{6.6a}
\]

Both newborn singleton targets also have literal occurrences
(indeed \(\alpha\) occurs in the new left central position and at the far
right collar, while \(\gamma\) occurs at the far left collar and in the new
right central position).

### Theorem 6.1 (no-reset algebraic closure, with a residence horizon)

Under (6.1)--(6.6), every child owner, pre-row cell, native lower and upper
q1 cell, and pivot ray has the standard Pascal value.  Signed residence
also holds provided the inherited shared-bank labels satisfy the horizon
condition below.  On a plateau the two enriched one-cell values and their cap objects
acquire \(\beta\); on a jump they persist literally.  No additional cap
address or de-enrichment guard is created.

More explicitly, on a plateau the cell \(X\) stays fixed, while

\[
 P_i\mapsto P_i+\beta,\qquad S_i\mapsto S_i+\beta
       \quad(1\le i<h).                                \tag{6.6b}
\]

The old-coordinate owner traces are unchanged and \(\beta\) is present
throughout the packet.  On a jump, \(X,P_i,S_i\) for \(i<h\) persist
literally and the two new top rays are \(P'_h=M_0\) and \(S'_h=M_h\).
The ordered right suffix is transported literally as

\[
 \omega_H=(\omega_h,\{\alpha\}),                       \tag{6.6c}
\]

not merely through equality of its total union.

If \(1\le j<h\) and \(2\le s\le h\), then the inherited indices remain
legal forever:

\[
\begin{array}{c|c|c}
 &\text{left index}&\text{right index}\\ \hline
\text{plateau}&j<h&s\le h,\\
\text{jump}&j+1<H&s<H.
\end{array}                                             \tag{6.7}
\]

Hence the exported negative-cap state contains exactly two logical
positions in every descendant.  Its *address count* does not accumulate
with the number of deadline jumps.  This does not mean that the complete
signed-residence trace persists forever.

For completeness, an exceptional singleton-shore seam mode from Theorem
1.2 is likewise retained at the same logical seam on both a plateau and a
jump.  The canonical interior recurrence above is preferable because its
two literal indices are given by (5.1) and (6.6a).

#### Proof

On a plateau, substitute \(B',C'\) into the source formula.  Every local
owner and pre-row target gains \(\beta\), and the two enriched letters gain
it at the same source positions, so the proof of Theorem 1.1 is unchanged.
On a jump, (6.5) is an equality of source blocks.  The menu-independent
Pascal identities give

\[
 M'_0=M_0+\alpha,\qquad
 M'_t=M_{t-1}\cup M_t\ (1\le t\le h),\qquad
 M'_H=M_h+\gamma,
\]

with the analogous collar identities.  Theorem 1.1 applied at depth \(H\)
then gives both native q1 palettes and the standard child rays.  Residence
for labels confined to one bank follows as before; labels shared by the
recursively nested banks require the additional horizon audit below.
The two parent enriched letters occur unchanged in (6.5), so their
one-cell occurrences persist.  More generally, an interval lying wholly
inside \(E_h^-\), wholly inside \(A_h^-(j)[X]A_h^+(s)\), or wholly inside
\(E_h^+\) persists literally.  An old interval crossing
\(E_h^-|A_h^-(j)\) acquires the inserted \(\alpha\), and one crossing
\(A_h^+(s)|E_h^+\) acquires the inserted \(\gamma\); those are ambient
sector transports, not literal preservation claims.  The index
inequalities in (6.7) are immediate. \(\square\)

The theorem is local and exact.  An arbitrary mixed exterior row or a
different global Pascal-sector assignment may still reject the inherited
state; that happens precisely through the screened equations of Theorem
4.1.  It is an ambient target-transport obstruction, not a need to reset
the \(K_2\) locations.  In particular, on a plateau an untagged parent
target \(H_L(j)\) or \(H_R(s)\) is not supplied by its now-\(\beta\)-tagged
letter; if that untagged sector remains required it needs another
occurrence.  The singleton targets \(\{\lambda_j\},\{\rho_s\}\) were
already absent from the enriched local source and retain their pre-existing
alternate-host obligation.  These are old-target sector rows, not new
\(K_2\) cap objects.

### Theorem 6.2 (sharp shared-bank residence horizon)

Start from pairwise-disjoint banks at depth \(h_0\), and perform \(t\)
deadline jumps, so the current depth is \(h=h_0+t\).  For the labels
\(\alpha_i,\gamma_i\) born at jump \(i\), their two source occurrences have
separation and internal zero-gap

\[
 \Delta_i=3h_0+t+2i,qquad g_i=\Delta_i-(h+1)=2h_0+2i-1. \tag{6.7a}
\]

Their complete local owner traces are

\[
\begin{aligned}
 \operatorname{tr}(\alpha_i)
   &=0^{t-i}1^{h+1}0^{g_i}1^{t-i+1},\\
 \operatorname{tr}(\gamma_i)
   &=1^{t-i+1}0^{g_i}1^{h+1}0^{t-i}.
                                                               \tag{6.7b}
\end{aligned}
\]

The label is signed-resident exactly when

\[
                         t\le h_0+2i-2.                \tag{6.7c}
\]

Consequently the whole inherited packet is resident exactly through
\(t\le h_0\); the first failure is the oldest pair at jump \(h_0+1\).
Plateaux and changing the active enrichment indices alter neither
\(\Delta_i\) nor \(g_i\).

#### Proof

At time \(t\), \(\alpha_i\) has within-bank indices \(t-i+1\) in the
left central bank and \(h_0-1+i\) in the right exterior bank.  Reading
their absolute source positions in (6.5) gives \(\Delta_i\); the two
\(\gamma_i\) positions give the same separation.  Each occurrence supports
exactly \(h+1\) consecutive owners, so the owners strictly between the two
positive runs number \(g_i\).  Since this zero-run is internal, residence
is equivalent to \(g_i\ge h+1\), which is (6.7c).  The displayed traces
record the clipped portions before and after those two runs. \(\square\)

For \(h_0=2,t=3\), the first bad traces are

\[
 0^2 1^6 0^5 1^3,qquad 1^3 0^5 1^6 0^2,              \tag{6.7d}
\]

whose internal zero-run has length five rather than six.  No exterior
prefix or suffix repairs it while the packet remains contiguous.

If a genuine literal rebase at depth \(b\) restores disjoint banks with
the same exported interface, exactly \(b\) further jumps are safe; the
latest full-rebase depths are \(2b,4b,8b,\ldots\).  This needs one countdown
field but no bounded-support rebase is proved.  In a rolling scheme the
pair born at index \(i\) expires at \(t_i=b+2i-1\), so after the first
forced service before jump \(b+1\), one older pair reaches deadline every
two jumps.

A longer recursive construction therefore needs a physical shared-bank
rebase, a nonlocal rethread, or a nonflat residence actuator.  A fresh
choice of the two enrichment sites alone does not move the two occurrences
in (6.7a) and cannot repair the gap.  The independent audit is
`MATH_AUDIT_AD_INHERITED_K2_RECURRENCE_AND_SHARED_BANK_RESIDENCE_HORIZON_20260801.md`.

For comparison, the locally legal fresh transition
\((j,s)\mapsto(1,H)\) enriches \(\alpha,\gamma\) but thins the two old
letters.  Already at \(h=2\) it can delete the old targets

\[
       (B-\{x_R\})+\lambda_1,\qquad
       (B-\{x_L\})+\rho_2.                              \tag{6.8}
\]

Such a fresh reset is optional and is zero-debt iff the displaced targets
have a replacement occurrence assignment whose complete row bank passes
Theorem 4.1.  This optional reset criterion is no longer an essential local
recurrence gate.

### Lemma 6.3 (upper exterior needs no enrichment-site reset)

Let a literal continuation accepted by Theorem 3.1 have owner row
\(V_i=(D^hA)_i\).  For every \(q\ge1\) and every valid start \(i\),

\[
 (D^{h+q}A)_i
   =\bigcup_{t=i}^{i+q}V_t.                             \tag{6.9}
\]

Consequently the continuation is upper-exact through depths in a set
\({\cal Q}\) iff, for every \(q\in{\cal Q}\), its consecutive
\((q+1)\)-owner unions cover the required rank-\((r+q)\) targets.  This
criterion includes intervals crossing the pivot/exterior boundary and is
independent of whether the \(K_2\) state was freshly reset.

#### Proof

Both sides of (6.9) are the union of the source letters with indices
\(i,i+1,\ldots,i+h+q\). \(\square\)

Thus a one-ended continuation can generate a fully upper-exact exterior
without a fresh enrichment-site reset, provided its source-compatible owner chronology has
the stated consecutive-union deck.  Constructing such a chronology while
also satisfying the lower occurrence matching and the screened common cap
is still the global gate.

## 7. Exact additive-one prefix-extension theorem

Let

\[
                         B(k)=W+h.
\]

A source word of length \(B(k)+1=W+h+1\) has \(W+1\) depth-\(h\) cells.
After the \(4h+1\)-letter pivot prefix, append exactly

\[
                         n=W-3h                           \tag{7.1}
\]

letters.  The first \(n-1\) new depth cells must supply the remaining
\(W-3h-1\) distinct owners; the last cell is the unique surplus cell.

### Theorem 7.1 (one-ended global extension iff)

The fixed \(K_2(j,s)\) prefix extends to a literal length-\(B(k)+1\)
construction with:

* \(W\) distinct owners forming an upper-surjective alternating Hamilton
  path;
* native lower and upper q1 support;
* signed residence, with clipping allowed only at the two global ends;
* a prescribed occurrence-perfect lower compiler and prescribed terminal
  surplus target;
* every declared mixed upper/cap guard;

iff there are

1. an owner order beginning with (1.3) whose rooted incidence edges satisfy
   the exact perfect/near-perfect matching rows, all upper-colour rows, and
   the graphic spanning-tree rows;
2. an occurrence matching extending the forced prefix/ray bank;
3. \(n\) appended nonempty source letters such that the first \(n-1\)
   owner steps are accepted by Theorem 3.1 and the last step realizes the
   prescribed surplus row; and
4. the combined owner, q1, matching, surplus, and guard row family passes
   Theorem 4.1.

When these conditions hold, concatenating the prefix with the maximal word
from Theorem 4.1 is the desired literal source.  Conversely, every such
source induces items 1--4.

#### Proof

Necessity follows by reading the owner path, selected target occurrences,
source suffix, run ages, and exact row equations from the word.  For
sufficiency, Theorem 4.1 gives one common source with the prefix fixed.
Theorem 3.1 certifies its source chronology, native q1 equalities, and
residence.  Item 1 supplies the owner topology and immediate upper
surjectivity; item 2 supplies the lower target injection; the declared
remaining rows give the surplus and wider guards.  The count (7.1) gives
total length \(B(k)+1\). \(\square\)

Theorem 7.1 is an exact characterization, not an existence proof.  The
fixed-\(H\) protected-factor theorem supplies only abstract set-valued
incidence containment and does not imply items 3--4.

## 8. Remaining gate

The strongest unconditional conclusions are:

1. two enriched positions are enough and are minimal;
2. the literal prefix exports an exact finite continuation state;
3. first-owner continuation has the forced port (2.5);
4. frozen-prefix source/cap/matching feasibility is exactly (4.3);
5. the inherited \(K_2\) *address/cap algebra* closes under plateaux and
   deadline jumps without a fresh enrichment-site reset or growing cap
   count, while signed residence has the sharp horizon (6.7c);
6. upper exterior coverage is exactly the owner-union condition (6.9), so
   it does not require an enrichment-site reset;
7. absolute maximal erosion and automatic fresh reset are false.

The missing positive theorem is now precise:

> construct an upper-surjective rooted Hamilton path and occurrence
> matching extending the pivot prefix such that their owner sequence is
> accepted by the ordered-suffix/run-age automaton and their complete row
> bank passes frozen-prefix relative maximal erosion, together with a
> shared-bank rebase/rethread before the horizon expires.

There is no remaining local enrichment-location reset hypothesis.  The
unresolved recursive issue is global transport of the old target sectors,
the lower occurrence matching, and their one common cap through the
inherited state, plus regeneration of the shared-bank residence trace.

No abstract factor embedding, standalone residence proof, or marginal Hall
theorem implies this joint condition.
