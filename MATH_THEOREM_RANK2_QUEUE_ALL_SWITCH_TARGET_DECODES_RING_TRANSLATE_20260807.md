# Every all-switch proper target decodes its ternary ring translate

**Date:** 2026-08-07  
**Method:** read active omitted labels and inactive common-singleton labels
phase by phase  
**Status:** unconditional fixed-frame recoupling theorem. With all bank
switches, the proper-depth target inventories of all distinct translated
queue rings in one ternary frame are pairwise disjoint. This holds for
any fixed core injection and includes the cyclic wrap signs. Cross-frame
target collisions remain open.

## 1. State and source conventions

Fix one ternary frame with ordered triples

\[
 T_b=\{x_{b,0},x_{b,1},x_{b,2}\},
 \qquad b\in\mathbb Z_p,
\tag{1.1}
\]

and identify owner states with omission vectors in
\(\mathbb F_3^p\). Put

\[
 P_a=e_0+\cdots+e_{a-1},
 \qquad P_0=0.
\tag{1.2}
\]

The standard \(3p\)-cycle translated by \(v\in\mathbb F_3^p\) has,
immediately before the phase-\(a\) update in round \(q\), state

\[
 v+q\mathbf1+P_a.
\tag{1.3}
\]

The update adds \(e_a\). Its literal source block in phase \(a\) is

\[
 T_a\setminus\{x_{a,v_a+q+1}\}.
\tag{1.4}
\]

The translated ring depends only on

\[
 [v]\in\mathbb F_3^p/\langle\mathbf1\rangle,
\tag{1.5}
\]

because advancing one complete round replaces \(v\) by
\(v+\mathbf1\).

Fix any injection of the \(3p\) bank coordinates into distinct core
coordinates, and apply all \(3p\) core--bank carrier-interior switches.
Only the core part depends on this injection. The bank part of every
proper target has two coordinates in each active phase and the unique
carrier-interior singleton in each inactive phase.

## 2. Exact decoder, including wrap

Let \(Q\) be a proper source interval of length

\[
 1\le j<p
\tag{2.1}
\]

starting with phase \(a\) in round \(q\). Its active phases are the
proper cyclic interval

\[
 A=\{a,a+1,\ldots,a+j-1\}\pmod p.
\tag{2.2}
\]

For \(b\in\{0,\ldots,p-1\}\), define the wrap bit

\[
 \zeta_a(b)=
 \begin{cases}
  1,&b<a,\\
  0,&b\ge a,
 \end{cases}
\qquad
 \eta_a(b)=1+\zeta_a(b)\in\mathbb F_3.
\tag{2.3}
\]

Thus the first phase-\(b\) update weakly after the start of \(Q\) occurs
in round \(q+\zeta_a(b)\). Put

\[
 w=v+q\mathbf1.
\tag{2.4}
\]

### Theorem 2.1 (target-to-translate decoder)

From the value of the all-switch target on \(Q\), one recovers:

1. its active cyclic interval \(A\) and start phase \(a\);
2. the vector \(w\in\mathbb F_3^p\);
3. hence the translated ring
   \[
   [v]=[w]\in\mathbb F_3^p/\langle\mathbf1\rangle.
   \tag{2.5}
   \]

Explicitly, let \(r_b\in\mathbb F_3\) be:

- in an active phase, the label of the unique coordinate omitted from
  the target's two-subset of \(T_b\);
- in an inactive phase, the label of the target's singleton in \(T_b\).

Then

\[
 r_b=
 \begin{cases}
  w_b+\eta_a(b),&b\in A,\\
  w_b+\eta_a(b)+1,&b\notin A,
 \end{cases}
\tag{2.6}
\]

and therefore

\[
 \boxed{
 w_b=
 \begin{cases}
  r_b-\eta_a(b),&b\in A,\\
  r_b-\eta_a(b)-1,&b\notin A.
 \end{cases}}
\tag{2.7}
\]

#### Proof

The phases in which the target meets \(T_b\) in two coordinates are
exactly the active phases; every inactive phase contributes one
all-switch singleton. Since \(A\) is a nonempty proper cyclic interval,
its set determines its unique start \(a\), namely the active phase whose
predecessor is inactive.

If \(b\in A\), its source update in \(Q\) occurs in round
\(q+\zeta_a(b)\). Formula (1.4) says that its active pair omits

\[
 v_b+q+\zeta_a(b)+1
 =w_b+\eta_a(b),
\]

which is the first row of (2.6).

If \(b\notin A\), the interval \(Q\) lies between the previous and next
phase-\(b\) updates. The next occurs in round
\(q+\zeta_a(b)\), so the two bounding source blocks omit, respectively,

\[
 v_b+q+\zeta_a(b)
 \quad\text{and}\quad
 v_b+q+\zeta_a(b)+1.
\]

Their common coordinate is the third ternary label

\[
 v_b+q+\zeta_a(b)+2
 =w_b+\eta_a(b)+1.
\]

The all-switch decoration inserts exactly this common coordinate in the
target. This proves the second row of (2.6), and (2.7) follows.
Finally \(w-v=q\mathbf1\), so \(w\) and \(v\) determine the same
translated ring. \(\square\)

## 3. Fixed-frame all-depth disjointness

### Corollary 3.1 (all translates have disjoint proper inventories)

Let \(R_v,R_{v'}\) be two distinct translated \(3p\)-rings in the same
frame:

\[
 [v]\ne[v']
 \quad\text{in}\quad
 \mathbb F_3^p/\langle\mathbf1\rangle.
\tag{3.1}
\]

After applying all bank switches, no proper-depth target of \(R_v\)
equals a proper-depth target of \(R_{v'}\). This remains true if the two
rings use different core injections.

#### Proof

Targets at different depths have different ranks. If equal targets at
the same proper depth existed, Theorem 2.1 would decode the same quotient
class from both values, contradicting (3.1). The decoder reads only the
bank intersections, so the core injections are irrelevant. \(\square\)

Since the translation stabilizer of the standard ring is
\(\langle\mathbf1\rangle\), one frame has exactly \(3^{p-1}\) distinct
translated rings. Corollary 3.1 says that all

\[
 3^{p-1}\cdot3p
\tag{3.2}
\]

targets in every fixed proper-depth row are distinct across that complete
translate family, even though the rings themselves overlap in owners.

In particular, any owner-disjoint ternary quotient cycle factor selected
inside one frame is automatically target-disjoint at **every** proper
depth after the all-switch decoration.

## 4. Consequence and exact boundary

The former fixed-frame target obstruction was caused by the canonical
source rule, which exposed only the active two-block and hid all inactive
phase states. The all-switch gauge writes one common singleton from every
inactive phase into every target. Those singletons are precisely the
missing address digits needed to decode the owner-ring translate.

Thus, inside each canonical owner frame, the two recoupling rows now close
simultaneously:

\[
 \boxed{
 \text{owner-disjoint quotient cycles}
 \Longrightarrow
 \text{all-depth target-disjoint decorated cycles}.}
\tag{4.1}
\]

What remains is exclusively cross-frame:

1. targets from two different canonical frames may still coincide;
2. q1 palettes are not yet proved disjoint between frames;
3. global cycle fusion and the residual compiler remain open.

No claim of global target disjointness or \(B(k)+O(1)\) follows from the
fixed-frame decoder alone.
