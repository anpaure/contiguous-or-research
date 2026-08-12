# The clean lag-two \(B+2\) route: shortest implication chain and the first unproved factor gate

**Date:** 2026-08-07  
**Status:** proof-safe synthesis plus one new packet-selection theorem.
The complete lag-two packets for the actual Ferrers boundary bank can be
chosen with all middle, lower-q1, and immediate-upper resources mutually
disjoint.  The first unproved implication is not local supply or
residence: it is extension of the resulting four-incidence-edge path bank
to one spanning middle-levels two-factor.  The currently frozen protected
factor theorem treats only the two-edge punctured projection, whose
literal packet exports a forced-coatom ticket.

## 1. Audited inputs

Use

\[
 n=2m+1,\qquad L=d+2,\qquad
 a=m-d-2,\qquad W=\binom{n}{m}.
\tag{1.1}
\]

The triangular Ferrers boundary has a task bank of size

\[
 h\le\binom{d+1}{2}=O(d^2)=O(m).
\tag{1.2}
\]

Each task is a flag

\[
 f=(M,U=M+u),\qquad |M|=a.
\tag{1.3}
\]

The clean lag-two fixed-core collar proves that one task has a literal
width-\(L\) realization containing, in one resident source history,

1. its saturated suffix \(M\subset U\);
2. the forced successor coatom \(Y=M+C+y\subset T_0\);
3. three consecutive rank-\(m\) owners

   \[
   T_-=M+C+u+x,\quad
   T_0=M+C+u+y,\quad
   T_+=M+C+y+v;
   \]

4. the two native lower-q1 colours

   \[
   I_-=M+C+u,\qquad I_+=M+C+y;
   \]

5. the two native immediate-upper colours

   \[
   J_-=M+C+u+x+y,\qquad
   J_+=M+C+u+y+v;
   \]

6. owner run and gap floor \(L\).

Thus the local packet has no immediate-palette or forced-coatom sidecar.

## 2. New theorem: all complete packets can be selected resource-disjointly

For one fixed flag, choose

\[
 C\in\binom{[n]\setminus U}{d}
\tag{2.1}
\]

and then ordered distinct

\[
 x,y,v\in[n]\setminus(U\cup C).
\tag{2.2}
\]

Put

\[
 N=m+d+2.
\tag{2.3}
\]

The exact menu size is

\[
 \boxed{D=\binom Nd(m+2)_3.}
\tag{2.4}
\]

The following are upper bounds on the number of menu items of this fixed
task containing one prescribed value, after forgetting the typed slot:

\[
\begin{aligned}
 \Delta_O
 &=
 2(d+1)(m+1)_2+(d+2)_2m,
 \\
 \Delta_L
 &=
 (m+2)_3+(d+1)(m+1)_2,
 \\
 \Delta_U
 &=
 2(d+2)_2m.
\end{aligned}
\tag{2.5}
\]

Here the three lines refer respectively to rank-\(m\) owners,
rank-\((m-1)\) lower colours, and rank-\((m+1)\) upper colours.

### Lemma 2.1 (per-task load audit)

The bounds (2.5) are valid.

#### Proof

For \(T_-\) or \(T_0\), a fixed owner contains \(U\).  Choose the
distinguished exchanged label from its \((d+1)\)-element difference with
\(U\), after which \(C\) is fixed, and choose the other two exterior
labels.  This gives \((d+1)(m+1)_2\) in either slot.

For \(T_+\), choose ordered \(y,v\) from the \((d+2)\)-element difference
with \(M\), after which \(C\) is fixed, and choose \(x\) outside
\(T_++u\).  This gives \((d+2)_2m\).

A fixed \(I_-=U+C\) fixes \(C\), leaving \((m+2)_3\) ordered exterior
labels.  For a fixed \(I_+=M+C+y\), choose \(y\) from its
\((d+1)\)-element difference with \(M\), then choose \(x,v\) outside
\(I_++u\), giving \((d+1)(m+1)_2\).

Finally, a fixed \(J_-\) or \(J_+\) contains \(U\).  Choose its two
ordered active labels from the \((d+2)\)-element difference with \(U\),
then choose the remaining exterior label, giving \((d+2)_2m\) in either
slot. \(\square\)

### Theorem 2.2 (complete clean-packet bank)

If

\[
 \binom Nd(m+2)_3
 >
 (h-1)\bigl(3\Delta_O+2\Delta_L+2\Delta_U\bigr),
\tag{2.6}
\]

then one can choose one complete clean lag-two packet for every task so
that all selected owners, lower-q1 colours, and immediate-upper colours
are mutually distinct within their respective ranks.

Condition (2.6) holds for every sufficiently large optimal parameter.

#### Proof

After \(t<h\) packets have been selected, at most \(3t\) owner values,
\(2t\) lower values, and \(2t\) upper values are occupied.  Lemma 2.1
shows that these forbid at most

\[
 t(3\Delta_O+2\Delta_L+2\Delta_U)
\]

items in the next task menu.  Greedy induction proves the first claim.

For the second, \(h=O(m)\) and the parenthesis in (2.6) is \(O(m^3)\),
so the right side is \(O(m^4)\).  Since \(d\ge2\) eventually,

\[
 \binom Nd(m+2)_3=\Omega(m^5).
\]

Thus (2.6) holds for all sufficiently large parameters. \(\square\)

The selected packets lift to pairwise incidence-vertex-disjoint paths

\[
 T_-\subset J_-\supset T_0\subset J_+\supset T_+
\tag{2.7}
\]

of four edges in the middle-levels graph \(ML_{m+1}\).

## 3. The first unproved implication

Let \(P\) be the union of the paths (2.7).  Then

\[
 \Delta(P)\le2,\qquad |E(P)|=4h.
\tag{3.1}
\]

The standard small-protected-factor theorem gives a spanning two-factor
containing \(P\) when

\[
 \boxed{4h\le m-1.}
\tag{3.2}
\]

Thus the complete clean packet bank already has an unconditional
two-factor host in every dimension satisfying (3.2).

For the full worst-case Ferrers range, however,

\[
 4h\le2d(d+1)
   =\left(\frac{\pi}{2}+o(1)\right)m,
\tag{3.3}
\]

which lies outside the theorem's \(m-1\) guarantee.

The protected \(B+2\) theorem currently in the repository avoids (3.3)
by protecting only a two-edge path per task.  That path is the punctured
projection, not the complete clean packet: its literal realization
exports the authoritative forced successor coatom.  It therefore cannot
replace the missing full-path extension.

### Exact \(f\)-factor form

Let \(G=ML_{m+1}=(X,Y;E)\), and put

\[
 b(v)=2-d_P(v).
\tag{3.4}
\]

A spanning two-factor \(F\supseteq P\) exists exactly when the residual
graph \(G-P\) has a bipartite \(b\)-factor.  By max-flow/min-cut, this is
equivalent to

\[
 \boxed{
 e_{G-P}(S,Y\setminus T)+b(T)\ge b(S)
 \quad(S\subseteq X,\ T\subseteq Y).}
\tag{3.5}
\]

Equation (3.5) is the exact first missing theorem for the selected clean
bank.  Because the packet menus are still available during selection, a
sufficient all-\(m\) result may co-select \(P\) so that all cuts (3.5)
hold; it need not extend every adversarial four-edge path bank.

There is a useful cancellation specific to a prescribed subgraph.  Since

\[
\begin{aligned}
 d_P(S)&=e_P(S,T)+e_P(S,Y\setminus T),\\
 d_P(T)&=e_P(S,T)+e_P(X\setminus S,T),
\end{aligned}
\]

condition (3.5) is equivalently

\[
 \boxed{
 e_G(S,Y\setminus T)+2(|T|-|S|)
 \ge e_P(X\setminus S,T).}
\tag{3.6}
\]

Writing \(A=X\setminus S\), \(B=T\), and
\(r=m+1\) for the degree of \(ML_{m+1}\), this becomes

\[
 \boxed{
 e_G(A,B)+(r-2)(W-|A|-|B|)
 \ge e_P(A,B)
 \quad(A\subseteq X,\ B\subseteq Y).}
\tag{3.7}
\]

Thus the protected-factor problem is not an opaque two-factor question:
the exact damage on every cut is simply the number of selected packet
incidences lying inside \(A\times B\).  A co-selection theorem need only
spread those incidences below the deterministic middle-level cut margin
on the left side of (3.7).

## 4. Classification of the missing factor theorem

The implication

\[
 \boxed{
 \text{selected complete clean packet bank}
 \Longrightarrow
 \text{protected spanning middle-levels two-factor}}
\tag{4.1}
\]

is **not** an off-the-shelf consequence of the Middle Levels Theorem.
Hamiltonicity of \(ML_{m+1}\) does not imply that an arbitrary prescribed
linear forest lies in a Hamilton cycle or even in a two-factor.

Nor does the existing small-protected theorem cover the worst permitted
bank, because of (3.3).  Arbitrary protected banks beyond its threshold
can concentrate on a tight residual cut, so a theorem with no structural
hypothesis would be unsafe.

The most accurate classification is:

> (4.1) is a plausible new co-selected protected-\(f\)-factor lemma.

It is substantially weaker than the original OR-word problem.  It
contains no literal width-\(L\) antecedent for the unprotected edges, no
Hamilton/component requirement, no arbitrary-width upper deck, and no
lower compiler.  Its exact content is only the cut system (3.5).

## 5. Shortest exact implication chain to \(B+2\)

The proof-safe chain is now:

1. **Ferrers task extraction — proved.**  
   Obtain \(h\le\binom{d+1}{2}\) promotion flags.

2. **Complete local packet — proved.**  
   The clean fixed-core collar realizes every flag, forced coatom, three
   owners, both immediate palettes, and local residence at width \(L=d+2\).

3. **Joint named-resource selection — proved here.**  
   Theorem 2.2 chooses all complete packets with disjoint owner, lower,
   and upper values.

4. **Protected two-factor completion — first open implication.**  
   Prove (3.5) for a co-selected packet bank.  It is already proved under
   the additional scalar condition \(4h\le m-1\).

5. **Connected literal serialization — open.**  
   Turn the protected two-factor into one opened chronology having a
   common width-\(L\) source antecedent.  The fixed collars certify only
   the protected portions.

6. **Deep upper and lower compilation — open.**  
   Preserve every upper target beyond rank \(m+1\) and cover the strict
   lower ideal on intervals of length at most \(L-1=d+1\), in the same
   source word.

7. **Decorated middle-levels implication — proved.**  
   Once Steps 4--6 hold, the resulting word has length

   \[
   W+d+2=B(2m+1)+2
   \]

   and is universal.

## 6. Verdict

The clean lag-two discovery eliminates the local promotion, immediate
palette, forced-coatom, and residence obstructions.  The actual boundary
bank is only \(O(m)\), and its complete packets can now be selected
resource-disjointly.

The first remaining statement is the protected \(f\)-factor cut
(3.5), not the full dynamic-cache theorem.  It is plausible and genuinely
smaller than the original problem, but it is not standard and it is not
the final obstacle.  Even a proof of (3.5) would still leave the global
literal serialization and all-depth compiler correlations.
