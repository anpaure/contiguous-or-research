# Safe de Bruijn quartet closure: exact neutralities and an exponential determinant obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

Use the safe de Bruijn model at protected depth \(d\), with

\[
                         2\le d\le H,\qquad \ell=H+d.
\tag{0.1}
\]

At root \(A\), arcs are injective ordered \(\ell\)-words in
\(U=A^c\); their first \(H\) letters give the complement-form middle
target. Root-local state conservation makes paths and cycles, while
global target rows impose capacity one.

The audited all-depth quartet exchange is a genuine physical move in
this model whenever four roots share one positional word and one retained
phase schedule. It is nevertheless insufficient to make the diagonal
port-pairing relaxation integral or to create a bounded-component cover.

This note proves four exact statements.

1. **Quartets are load- and component-neutral.** A synchronized quartet
   preserves every signed target load through depth \(d\), every root
   quota, and the number of phase-path components at each touched root.
   It can change port labels inside a fixed literal fibre, but cannot
   decrease a hole/collision objective or a component-count objective.

2. **Quartets act only after literalization.** Both sides of a quartet
   consist of four already labelled cyclic frames with one common
   positional schedule. The move is not defined on a clone flow whose
   incoming and outgoing target ports have not yet been paired. Treating
   it as such a move assumes the diagonal pairing one is trying to prove.

3. **The augmented matrix remains very far from TU.** For every integer
   \[
      1\le r\le
      \left\lfloor\frac{M+1}{H+2d+2}\right\rfloor,
   \tag{0.2}
   \]
   the safe state-incidence/target matrix contains a square minor of
   determinant
   \[
                             \boxed{\pm2^r.}
   \tag{0.3}
   \]
   These are actual disjoint root-local safe cycles. Appending every
   synchronized quartet column, every all-depth target row, and every
   common-schedule row cannot remove an existing submatrix. At
   \(d=H\), one may take \(r=\Theta(m/H)\), so the determinant magnitude
   is
   \[
                             2^{\Theta(m/H)}.
   \tag{0.4}
   \]

4. **The obstruction is outside the audited parity quotient.** Quartet
   sign characters on tops have only the affine \(2m\)-dimensional
   quotient and are \(o(W)\)-cheap. The minors in (0.3) live instead in
   the ordered state/target port incidence. Correcting all top-sign
   syndromes leaves them unchanged.

Thus adding synchronized rectangles to the natural safe-de-Bruijn
formulation does not yield a network, a TU polytope, or a
bounded-component theorem. Quartets remain useful exact kernel moves for
later noncommuting surgery, but a positive proof needs an additional
operation which changes loads or phase-run structure while preserving
literal diagonal ports.

## 1. Safe scheduled frames

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 \mathcal A=\binom V{m-H}.
\tag{1.1}
\]

For \(A\in\mathcal A\), let \(U=A^c\). A labelled cyclic order

\[
                         \pi=(z_0,\ldots,z_{M-1})
\tag{1.2}
\]

and a retained phase set \(S\subseteq\mathbb Z_M\) define the middle
targets

\[
                         D_i=A\cup
 \{z_i,z_{i+1},\ldots,z_{i+H-1}\},
 \qquad i\in S.
\tag{1.3}
\]

At depth \(q\le d\), their signed flags are

\[
 L_{i,q}=A\cup\{z_{i+q},\ldots,z_{i+H-1}\},
\tag{1.4}
\]

\[
 R_{i,q}=A\cup\{z_i,\ldots,z_{i+H+q-1}\}.
\tag{1.5}
\]

Because the whole top order is injective, these are safe de Bruijn
states through every \(d\le H\).

Let

\[
                         c(S)
\tag{1.6}
\]

be the number of nonempty cyclic runs of \(S\). Cutting at the gaps
gives exactly \(c(S)\) promotion paths; if \(S=\mathbb Z_M\), cut once
and put \(c(S)=1\).

## 2. Exact action of a quartet on scheduled paths

Choose an \((M-2)\)-set \(C\), four outside labels

\[
                         a_0,a_1,b_0,b_1,
\tag{2.1}
\]

and the four tops

\[
                         U_{ij}=C\cup\{a_i,b_j\}.
\tag{2.2}
\]

Fix one cyclic positional word on \(C\cup\{P,Q\}\). On \(U_{ij}\), let
\(\pi_{ij}^+\) put \(a_i,b_j\) in positions \(P,Q\), and let
\(\pi_{ij}^-\) put \(b_j,a_i\) there. Use one common retained phase set
\(S\) and, when tags are present, one common phase-tag schedule.

The physical quartet replaces

\[
 (\pi_{00}^+,\pi_{01}^-,\pi_{10}^-,\pi_{11}^+)
 \longleftrightarrow
 (\pi_{00}^-,\pi_{01}^+,\pi_{10}^+,\pi_{11}^-).
\tag{2.3}
\]

### Theorem 2.1 (all-depth load and component neutrality)

Exchange (2.3) preserves exactly:

1. every middle target load;
2. both signed target-load vectors at every \(q\le d\);
3. every root occurrence quota and tag count;
4. the retained phase set at every touched root; and
5. the component count \(c(S)\) at each of the four roots.

In particular it preserves every objective depending only on target
loads and component counts.

#### Proof

Fix a phase and an interval length. If the positional interval contains
zero or both placeholders, the plus and minus target sets agree
individually. If it contains exactly one placeholder, the checkerboard
sum over \(i,j\) cancels: each \(a_i\)-term occurs with both signs as
\(j\) varies, and each \(b_j\)-term occurs with both signs as \(i\)
varies. Summing over the common retained phases and the interval lengths
\(H-q,H,H+q\) proves items 1--3.

The exchange changes only the labels occupying two fixed positions. It
does not change \(S\), its cyclic adjacency relation, or its runs. This
proves items 4--5. \(\square\)

### Corollary 2.2 (no autonomous descent)

A sequence of synchronized quartet exchanges cannot

1. reduce middle or entrance holes;
2. reduce repeat excess;
3. reduce aggregate signed-band discrepancy; or
4. reduce the number of promotion-path components.

It may only change the literal port realization within the common level
set of all these quantities.

This does not make quartets useless. It says precisely that they require
a second, noncommuting operation: first move within a load fibre by
quartets, then use a load-changing or component-splicing move whose
legality depends on the new ports.

## 3. Domain obstruction: a quartet is not a clone move

In the target-node relaxation, a middle target \(D\) has incoming ports
and outgoing ports indexed by ordered occurrences \(e\). Ordinary
conservation imposes only

\[
 \sum_{e:\kappa(e)=D}x_e^{\rm in}
 =
 \sum_{e:\kappa(e)=D}x_e^{\rm out}.
\tag{3.1}
\]

Literal diagonal pairing requires

\[
                         x_e^{\rm in}=x_e^{\rm out}
 \qquad\text{for every occurrence }e.
\tag{3.2}
\]

### Proposition 3.1 (quartet applicability requires (3.2))

The synchronized quartet (2.3) is defined only on states satisfying the
diagonal equations (3.2) at every retained phase of all four roots.
It gives no operation on a point satisfying only (3.1).

#### Proof

Each side of (2.3) is specified by four labelled cyclic orders. At a
retained phase, the incoming \((\ell-1)\)-state, the selected
\(\ell\)-word, and its outgoing \((\ell-1)\)-state are the prefix, whole
word, and suffix of that same order. Thus their occurrence indices
agree, which is exactly (3.2).

If (3.1) pairs the incoming half of occurrence \(e\) with the outgoing
half of \(f\ne e\), there is no labelled cyclic word at that phase.
Consequently neither a plus nor a minus frame in (2.3) is defined.
\(\square\)

Hence “round the port flow by quartet moves” is circular unless one first
proves a decomposition of the unpaired flow into literal quartet
domains. That decomposition is already a substantial form of the
diagonal-pairing theorem.

## 4. One determinant-two safe cycle

Let \(B_d\) be the block-diagonal root-state incidence matrix of the
safe de Bruijn graphs with memory \(\ell=H+d\), and let \(C_0\) be the
middle-target incidence matrix.

Fix one root \(A\). Choose distinct labels

\[
 a_0,\ldots,a_{H-1},\quad
 c_1,\ldots,c_d,\quad
 f_1,\ldots,f_{d+1}
\tag{4.1}
\]

in \(U=A^c\), and form the cyclic word

\[
 a_0,\ldots,a_{H-1},
 c_1,\ldots,c_d,
 a_0,\ldots,a_{H-1},
 f_1,\ldots,f_{d+1}.
\tag{4.2}
\]

Its length is \(2(H+d)+1=2\ell+1\). Every cyclic length-\(\ell\)
block is injective. The consecutive blocks therefore form a directed
safe de Bruijn cycle with distinct \((\ell-1)\)-states when \(d\ge2\).

Exactly two cycle arcs have the middle target

\[
                         D=A\cup\{a_0,\ldots,a_{H-1}\}.
\tag{4.3}
\]

Delete one node row from the incidence matrix of this directed cycle
and append row \(D\). On all cycle columns the resulting determinant is

\[
                             \pm2.
\tag{4.4}
\]

Indeed, the deleted cycle incidence has right kernel generated by the
all-ones vector, so the final determinant is, up to sign, the sum of row
\(D\) around the cycle, namely two.

## 5. Exponential minors survive quartet augmentation

We now place many copies of Section 4 without cross entries.

### Theorem 5.1 (determinant \(2^r\))

Let

\[
 1\le r\le
 \left\lfloor\frac{M+1}{H+2d+2}\right\rfloor.
\tag{5.1}
\]

For all sufficiently large \(m\), the matrix

\[
                         \begin{pmatrix}B_d\\C_0\end{pmatrix}
\tag{5.2}
\]

contains a square submatrix of determinant \(\pm2^r\).

#### Proof

Choose a common set

\[
                         K,\qquad |K|=m-H-1,
\tag{5.3}
\]

and distinct private labels \(p_1,\ldots,p_r\) outside \(K\). Put

\[
                         A_i=K\cup\{p_i\}.
\tag{5.4}
\]

The complement of \(K\) has \(M+1\) labels. Inequality (5.1) allows us
to choose, disjointly from all \(p_j\), pairwise disjoint special sets

\[
                         S_i,\qquad |S_i|=H+2d+1,
\tag{5.5}
\]

one for each \(i\). Since \(p_i\notin S_i\), one has
\(S_i\subset A_i^c\).

Inside root \(A_i\), use \(S_i\) to make the safe cycle of Section 4.
Let \(D_i=A_i\cup J_i\) be its twice-occurring target. A target colour
from root \(A_j\), \(j\ne i\), cannot equal \(D_i\): every such colour
contains \(p_j\), is formed using only \(S_j\) outside \(A_j\), and
therefore omits the private label \(p_i\), whereas \(D_i\) contains
\(p_i\).

Root-state rows are disjoint by definition, and the selected target rows
\(D_i\) have no entries in the other copies. The chosen submatrix is
therefore block diagonal with \(r\) blocks of determinant \(\pm2\).
Its determinant is \(\pm2^r\). \(\square\)

At full protected depth \(d=H\), condition (5.1) permits

\[
                         r=\Theta(m/H),
\tag{5.6}
\]

which proves (0.4).

### Corollary 5.2 (quartet columns do not restore TU)

Append to (5.2)

1. every synchronized quartet exchange column;
2. every signed-depth target row;
3. every common tag-schedule row; and
4. any further port or component rows.

As long as the original safe occurrence columns and their state/target
rows are retained, the augmented matrix still contains all minors from
Theorem 5.1. It is not TU, and its subdeterminants are not bounded by any
constant as \(m\to\infty\).

#### Proof

Appending rows or columns cannot delete a submatrix formed from the old
rows and columns. \(\square\)

This addresses the natural extended formulation in which quartets are
added as compound move variables. Quotienting out the quartet directions
is different: it identifies distinct literal port states. Such a
quotient is not a physical network state space unless one separately
proves that every later splice is invariant under the identification.
The all-depth quartet theorem proves load invariance, not splice
invariance.

## 6. Fractional obstruction and its scope

On each safe cycle in Theorem 5.1, put weight \(1/2\) on every arc.
Root-local conservation holds and the twice-used target has load one.
No nonzero integral circulation supported on that cycle satisfies its
target capacity: conservation forces a common integral arc value, and
value one uses the target twice.

Taking the product over the \(r\) copies gives \(r\) independent
half-integral circulation defects. Quartet augmentation does not change
their target loads, and a quartet is not defined on their unpaired
half-port states by Proposition 3.1.

Open paths may escape one copy by omitting at least one of its two
repeated-target arcs. This creates a path boundary and a root-quota loss
which must be replaced elsewhere. Therefore Theorem 5.1 is not, by
itself, an \(\Omega(W/H)\) lower bound on the component count. It is an
exact obstruction to TU and to autonomous quartet rounding.

## 7. Relation to quartet parity and the internal-quartet Hall cut

The unrestricted quartet sign lattice has only affine mod-two
characters

\[
                         w(U)=\alpha_0+\sum_{x\in U}\alpha_x.
\tag{7.1}
\]

At most \(2m\) exceptional one-top swaps repair these syndromes at
\(o(W)\) incidence cost. This remains correct.

The determinant blocks in Theorem 5.1 do not define a new linear sign
character on tops. They use

1. ordered \((H+d-1)\)-state rows;
2. two occurrences of one target on a safe local cycle; and
3. the diagonal identity of the incoming and outgoing occurrence ports.

They therefore survive after every affine top-sign syndrome is repaired.
This is the requested higher integral obstruction.

There is also no conflict with the audited full-internal-quartet Gaussian
Hall theorem. That theorem says a construction confined to fixed
coordinate quartets needs positive-density cross-quartet axes. The
present theorem allows the unrestricted physical quartet library and
still finds non-TU port blocks. The two obstructions live in different
quotients.

## 8. Exact construction boundary

The following implication remains valid.

> If one first constructs a literal safe tight-path cover with
> \(o(W/H)\) components, then synchronized quartets may be used freely to
> change its port realization without changing any target ledger or its
> component count.

What quartets cannot do alone is produce that initial cover from the
fractional target-node flow.

A positive proof now needs at least one additional move with one of the
following properties:

1. it changes a target load while preserving diagonal ports;
2. it splices components and changes the phase-run structure; or
3. together with quartets, it forms a proved Markov basis for the
   literal common-permutation fibre and has a quantitative route of
   length \(o(W/H)\).

The known transparent two-path switch is a candidate of type 2, but it
requires synchronized \(H+1\)-tails. No theorem supplies those tails at
the density needed to eliminate the blocks of Theorem 5.1.

## 9. Audited boundary

Proved here:

1. exact all-depth load neutrality of scheduled quartets;
2. exact invariance of the phase-run/component count;
3. the domain obstruction for applying quartets to unpaired clone flow;
4. actual safe-de-Bruijn minors of determinant \(2^r\);
5. determinant \(2^{\Theta(m/H)}\) at full protected depth;
6. persistence under every natural quartet-column augmentation; and
7. separation from the already-audited affine parity quotient.

Not proved here:

1. a bounded-component safe tight-path cover;
2. integrality of any substantially different quartet-orbit extended
   formulation;
3. a Markov-basis theorem combining quartets with transparent tail
   switches; or
4. coefficient one.

The verdict is therefore negative for quartet closure alone. The
all-depth quartet is an exact and valuable holonomy move, but it is
kernel-flat in both target loads and component schedule. It cannot by
itself repair diagonal port pairing, and the natural augmented matrix
has exponentially large subdeterminants.

## 10. Dependency ledger

The safe path and diagonal-port formulation is
MATH_THEOREM_PROMOTION_TIGHT_PATH_DEBRUIJN_TU_AND_PORT_PAIRING_OBSTRUCTION_20260726.md.
The synchronized all-depth quartet is
MATH_THEOREM_PROMOTION_RING_QUARTET_HOLONOMY_EXCHANGE_20260726.md,
with its scope audited in
MATH_AUDIT_COMMON_PERMUTATION_CONTAINMENT_AND_QUARTET_HOLONOMY_20260726.md.
The fixed internal-quartet Gaussian Hall cut is audited in
MATH_AUDIT_FULL_INTERNAL_QUARTET_GAUSSIAN_HALL_20260726.md.
