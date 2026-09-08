# Power-of-two antipodal selectors: the exact `m=2` exception and a positive `m=4` base

Date: 2026-07-31  
Status: exact finite theorem at (m=2,4); explicit positive complement-antipodal
(m=4) witness; no (m=8) or all-power-of-two existence claim

## 0. Verdict

The literal statement

> for every (m=2^a), one complement-antipodal middle-levels cycle has an
> upper occurrence SDR whose doubled positions have odd cyclic gaps, carry a
> protected (0^4) socket, and induce a leaf-peelable full gap graph

is false at (m=2).  The obstruction is not palette Hall: all three upper
choices have odd gaps and a leaf-peelable gap graph.  It is exactly the trace
face.  Here (Q=3), so a protected (0^4) socket is impossible, and the only
trace type is (100) up to rotation: its zero-run has length two and its
one-run has odd length one.

After treating (m=2) as a base exception, the proposed state is nonempty at
(m=4).  This note gives an explicit complement-antipodal
({\rm ML}(7)) Hamilton cycle and 117 upper occurrence SDRs which pass all
three requested gates.  For the lexicographically first witness, the full
gap--lower-colour graph has 42 vertices, 29 edges, thirteen tree components,
and a unique perfect matching obtained by literal leaf peeling.

There is also an exact warning.  A second complement-antipodal
({\rm ML}(7)) Hamilton cycle has both turn words surjective, but none of its
5,184 upper occurrence SDRs has odd doubled gaps.  Thus complement symmetry
does **not** rescue the already-refuted inference from marginal turn
surjectivity.  The cycle and occurrence transversal must be chosen jointly.

## 1. The standard double-cover model

Let (O=(O_0,\ldots,O_{Q-1})) be a Hamilton cycle of the odd graph
(KG(2m-1,m-1)), where

\[
                  Q=\binom{2m-1}{m-1}.
\]

When (Q) is odd, define

\[
 A_i=O_{2i},\qquad B_i=\overline{O_{2i+1}}
 \quad (i\in\mathbb Z_Q).
\tag{1.1}
\]

Then

\[
       A_i\subset B_i\supset A_{i+1}
\]

is a Hamilton cycle of ({\rm ML}(2m-1)).  With (s=(Q-1)/2), it obeys

\[
 \overline{A_i}=B_{i+s},\qquad
 \overline{B_i}=A_{i+s+1}.
\tag{1.2}
\]

Put

\[
 \ell_i=A_i\cap A_{i+1},\qquad
 u_i=B_{i-1}\cup B_i.
\tag{1.3}
\]

Then

\[
                         \overline{u_i}=\ell_{i+s}.
\tag{1.4}
\]

Consequently an upper occurrence SDR (I) forces the lower occurrence SDR
(J=I+s).  By the odd-gap antipodal-selector theorem, these representatives
alternate physically exactly when every cyclic gap of

\[
                            S=2I\pmod Q
\tag{1.5}
\]

is odd.

## 2. The exact (m=2) exception

At (m=2), (O=(1,2,4)) is the triangle (KG(3,1)).  There is one upper
turn colour, occurring at all three positions, so there are three upper
occurrence SDRs.  For each of them (S) is a singleton in (mathbb Z_3).
Its sole cyclic gap has length three, hence the odd-gap condition holds.
The forced one-by-one gap graph is a tree and leaf-peels.

But its trace is, up to rotation,

\[
                              z=100.
\]

It has one zero-run of length two and one one-run of odd length one.  It is
therefore exactly on the cycle face of the antipodal trace theorem.  In
particular there cannot be four consecutive unmarked positions in a word of
length three.  Hence no (m=2) selector satisfies the requested conjunction.

This is the smallest possible counterexample and should be isolated as a
base exception, not fed into a recursive protected-socket invariant.

## 3. An explicit positive (m=4) witness

Use the following Hamilton cycle of (KG(7,3)):

```text
7 88 38 73 52 11 112 14 81 42 84 35 76 50 13 82 37 74
49 70 41 22 97 28 67 44 19 104 21 98 25 100 26 69 56
```

Every entry has rank three, every rank-three mask occurs once, and consecutive
entries, including the last and first, are disjoint.  Apply (1.1).  The upper
and lower turn words each cover their complete 21-colour alphabet.  The upper
turn loads have histogram

\[
                  1^9\,2^{10}\,3^2,
\]

so there are (1^9 2^{10}3^2=9,216) upper occurrence SDRs.

Choose

\[
\begin{split}
 I=\{&0,1,2,3,5,7,8,11,12,13,14,18,19,20,21,23,\cr
     &25,26,29,30,31\}.
\end{split}
\tag{3.1}
\]

Then

\[
\begin{split}
 S=2I=\{&0,1,2,3,4,5,6,7,10,11,14,15,16,17,22,23,\cr
          &24,25,26,27,28\}\pmod {35},
\end{split}
\tag{3.2}
\]

whose cyclic gap lengths are

\[
 1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,1,1,1,1,1,7.
\tag{3.3}
\]

They are all odd.  The gaps of lengths five and seven give unmarked runs of
length four and six, so the trace has a protected (0^4) socket.  The forced
lower occurrence set is

\[
\begin{split}
 J=I+17=\{&0,1,2,3,5,7,8,11,12,13,17,18,19,20,22,24,\cr
            &25,28,29,30,31\}\pmod {35}.
\end{split}
\tag{3.4}
\]

There is exactly one member of (J) in each cyclic (I)-gap, and the lower
turn colours at those members are all distinct.  Construct the **full** gap
graph by joining each of the 21 gaps to every lower turn colour occurring in
it.  It has 29 edges on 42 vertices.  Exact union-find finds no cycle, so it
has (42-29=13) components.  Its displayed forced perfect matching covers
all vertices; equivalently, direct leaf deletion removes all 21 pairs.
Therefore the full graph is a balanced forest with a unique leaf-peelable
perfect matching.

This proves the requested (m=4) existential gate without using separate
turn-surjectivity as a sufficiency assumption.

## 4. Complete selector census on the positive cycle

The exact audit enumerates all 9,216 upper occurrence SDRs on the displayed
cycle.

| property | count |
|---|---:|
| doubled positions have all odd cyclic gaps | 135 |
| full gap graph is a balanced leaf-peelable forest | 135 |
| additionally has a protected (0^4) socket | 117 |

Thus on this one cycle leaf-peelability costs nothing beyond odd-gap
alternation.  The protected socket is stronger than the exact trace test and
removes eighteen selectors.  This is a finite property of this fixture, not
an all-(m) theorem.

Among the 117 joint witnesses, their full gap graphs have edge census

\[
                  26^5\,27^{28}\,28^{52}\,29^{32}.
\]

## 5. Surjectivity control: exact failure on another antipodal cycle

For comparison, use

```text
7 112 11 84 41 22 104 21 42 69 56 70 49 14 97 26 100 25
98 28 67 52 74 37 82 13 50 73 38 81 44 19 76 35 88
```

as the odd-graph Hamilton cycle in (1.1).  Its upper and lower turn words are
again both surjective.  Its upper occurrence domains give exactly 5,184
upper SDRs.  Exhaustive enumeration finds

\[
       \boxed{\text{zero SDRs whose doubled positions have all odd gaps}.}
\]

This is an exact complement-antipodal analogue of the general gap--Hall
warning: even after one shore forces the other by complement, the occurrence
interlacing condition remains genuine.

## 6. Scope and remaining theorem

What is proved here:

1. the protected-socket formulation has a genuine (m=2) base exception;
2. the complete requested state exists at (m=4);
3. marginal two-turn surjectivity remains insufficient under complement
   symmetry.

What is **not** proved:

* that a prescribed published or recursively generated antipodal cycle is
  selectable;
* that the (m=4) witness extends to (m=8);
* that leaf-peelability follows from odd gaps on any other cycle; or
* an all-power-of-two construction.

The corrected power-of-two target is therefore:

> use (m=2) as a separate terminal base, and for every power of two
> (m\ge4), construct the complement-antipodal cycle and its occurrence SDR
> jointly while carrying odd gaps, one trace breaker (not necessarily a
> (0^4) socket), and the graphic attachment invariant of the full gap
> forest.

The (m=4) census proves this state is nonempty and robust at the first
nontrivial power, but does not supply the induction.

## 7. Reproducibility

Run:

```bash
python3 scratch/audit_catalan_power_two_antipodal_selector_20260731.py
```

The script independently checks both odd-graph Hamilton cycles, their
middle-levels lifts and complement actions, both turn palettes, every upper
occurrence SDR, the forced lower representatives, every full gap graph,
union-find acyclicity, and literal leaf peeling.

Artifacts:

* `scratch/audit_catalan_power_two_antipodal_selector_20260731.py`
* `scratch/catalan_power_two_antipodal_selector_20260731.audit.json`

Exact hashes are reported after the final note is frozen and the audit is
rerun.
