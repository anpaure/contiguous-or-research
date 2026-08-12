# The punctured \(B+2\) boundary bank embeds in an exact protected middle-levels two-factor

**Date:** 2026-08-07  
**Status:** unconditional for all sufficiently large parameters.  Every
Ferrers-boundary flag task can be given a mutually resource-disjoint
punctured central edge, and the resulting bank extends to a spanning
middle-levels two-factor.  The punctured source still exports one
authoritative forced-coatom ticket per task.  Connectedness, that ticket
bank, the complete lower rainbow, the literal antecedent, and deeper upper
coverage remain open.

## 1. Parameters and task count

Put

\[
 n=2m+1,\qquad L=d+2,\qquad a=m-d-2,
\tag{1.1}
\]

and let \(h\) be the number of selected cells in the triangular Ferrers
boundary.  By construction,

\[
 \boxed{h\le\binom{d+1}{2}.}
\tag{1.2}
\]

Each task is a fixed flag

\[
 f=(M,U=M+u),\qquad |M|=a.
\tag{1.3}
\]

No asymptotic density assumption on the task bank is used below.

## 2. Projected central-edge menu

For a fixed flag, choose

\[
 C\subset[n]\setminus U,qquad |C|=d,
\tag{2.1}
\]

then choose ordered distinct labels

\[
 x,y\in[n]\setminus(U\cup C).
\tag{2.2}
\]

Put

\[
 I=U+C,
\quad
 T_-=I+x,
\quad
 T_0=I+y,
\quad
 J=I+x+y.
\tag{2.3}
\]

Then \(T_-,T_0\) are rank-\(m\) Johnson neighbours, \(I\) is their
rank-\((m-1)\) lower colour, and \(J\) is their rank-\((m+1)\) upper
colour.  The two incidences

\[
 T_-\subset J\supset T_0
\tag{2.4}
\]

form a two-edge path in the middle-levels graph on \([2m+1]\).

Put

\[
 N=m+d+2.
\tag{2.5}
\]

The exact menu size is

\[
 \boxed{D=\binom Nd(m+2)_2.}
\tag{2.6}
\]

Every menu item has a punctured literal realization.  Indeed, choose any
\(d\)-set \(A\subset M\), any \(a_0\in A\), and any \(z\in C\), and use
the core-swap source from
`MATH_THEOREM_PBBS_BPLUS2_SHIFTED_HINGE_ENDPOINT_HOLE_AND_CORE_SWAP_REPAIR_20260807.md`.
This realizes the displayed central owner/lower/upper path, not the full
promotion ticket: the forced successor coatom \(M+C+y\) is shortened by
the puncture and must be supplied separately.

## 3. Exact collision loads inside one fixed menu

Fix the task flag \((M,U)\).

* A prescribed rank-\((m-1)\) lower value occurs in at most

  \[
  (m+2)_2
  \tag{3.1}
  \]

  menu items.  It must contain \(U\), after which \(C\) is fixed.

* A prescribed rank-\(m\) owner occurs, in either owner slot, in at most

  \[
  2(d+1)(m+1)
  \tag{3.2}
  \]

  menu items.  In a specified slot, choose the distinguished exchanged
  label from the \((d+1)\)-set outside \(U\), and then choose the other
  exterior label outside the owner.

* A prescribed rank-\((m+1)\) upper value occurs in at most

  \[
  (d+2)_2
  \tag{3.3}
  \]

  menu items.  Its difference from \(U\) determines \(C\) after the
  ordered pair \((x,y)\) is selected.

These are literal per-task bounds; they do not rely on averaging over the
flag bank.

## 4. Greedy protected-bank selection

### Theorem 4.1

Suppose

\[
 \binom Nd(m+2)_2
 > (h-1)\left[
 4(d+1)(m+1)+(m+2)_2+(d+2)_2
 \right].
\tag{4.1}
\]

Then one can select one menu item for every task so that all selected
rank-\(m\) owners, rank-\((m-1)\) lower colours, and rank-\((m+1)\)
upper colours are mutually distinct within their respective ranks.

#### Proof

After \(t<h\) choices, at most \(2t\) owners, \(t\) lower colours and
\(t\) upper colours are occupied.  Equations (3.1)--(3.3) show that they
forbid at most

\[
 t\left[
 4(d+1)(m+1)+(m+2)_2+(d+2)_2
 \right]
\]

items in the next menu.  Under (4.1), at least one item remains.  Induct
over the tasks. \(\square\)

### Corollary 4.2

Condition (4.1) holds for all sufficiently large optimal parameters.

#### Proof

Here \(d=\Theta(\sqrt m)\) and \(h=O(d^2)=O(m)\).  For \(d\ge2\),
the left side of (4.1) is \(\Omega(m^4)\), whereas its right side is
\(O(m^3)\). \(\square\)

## 5. Exact two-factor extension

Let \(P\) be the union of the selected paths (2.4).  Resource
disjointness makes \(P\) a 2-bounded protected subgraph of the
middle-levels incidence graph \(ML_{m+1}\), with

\[
 |E(P)|=2h\le d(d+1).
\tag{5.1}
\]

Since \(d^2=(\pi/4+o(1))m\), one has

\[
 d(d+1)\le m-1
\tag{5.2}
\]

for all sufficiently large \(m\).  The protected-subgraph two-factor
theorem, applied with parameter \(m+1\), therefore extends \(P\) to a
spanning degree-two factor of \(ML_{m+1}\).

### Theorem 5.1 (protected boundary-bank factor)

For all sufficiently large optimal parameters, every Ferrers-boundary
promotion bank of size \(h\) has a choice of punctured \(B+2\) central
packets whose middle/upper incidence paths extend to a spanning
middle-levels two-factor.  The factor retains every selected task's named
set-valued owners and immediate upper colour, and hence its named lower
intersection.  Each protected path has the individual literal realization
of Section 2; this theorem does not place all those source blocks
simultaneously in one word.

## 6. Exact scope

The theorem closes the following row:

\[
 \boxed{
 \text{all }O(d^2)\text{ boundary promotions can be planted jointly in
 an exact middle/upper two-factor}.}
\]

It does **not** say that the resulting two-factor is one Hamilton cycle.
It also does not force the lower colours of the unprotected factor edges
to be rainbow, construct a common width-\(L\) source antecedent, preserve
all deeper upper intervals, supply the exported forced-coatom bank, or
solve the terminal lower compiler.

Thus the local/core-supply and abstract protected-factor obstruction are
gone for the actual triangular bank.  The surviving theorem is a
correlated factor lift:

\[
 \text{protected two-factor}
 \longrightarrow
 \text{one resident literal antecedent with all-depth palettes/compiler}.
\]
