# The Klein four-block `C8` is source-exact but lies outside the Catalan selector polytope

Date: 2026-08-01  
Lane: H/A, joint Catalan placement of the four-relabelled octagon  
Status: exact source/physical scope separation, exact forced-row obstruction,
and an exact conditional common-completion theorem.  No quotient weave or
additive-constant upper bound is claimed.

## 0. Verdict

Let `Q_d^0,Q_d^1` be the sharp octagon source blocks and put

\[
 \alpha=(a_0\ a_2),\qquad \beta=(a_1\ a_3).
\]

In block order `(1,beta,alpha,alpha beta)`, the phase exchange

\[
 0110\longleftrightarrow1001                                      \tag{0.1}
\]

is a genuine width-graded, context-transparent source relation.  Its
octagon action is `4g_8`, not zero, and its four blocks admit a pointwise
phase-common source cap.  Thus the new relation is real at source level.

It is **not** a physical Catalan-forest relation.  For every `d>=2`, either
literal endpoint of the four-block macro has

\[
\begin{array}{c|c|c}
 &\text{occurrences}&\text{distinct values}\\ \hline
\text{rank-}r\text{ owners}&32d+92&8d+24\\
\text{lower }q_1&32d+88&8d+24\\
\text{upper }q_1&32d+88&16.
\end{array}                                                   \tag{0.2}
\]

After duplicate physical edges are suppressed, the forced graph has

\[
 |V|=8d+24,\qquad |E|=8d+40,\qquad
 \deg=2^{8d}3^{16}4^8,                                     \tag{0.3}
\]

and is connected.  Its lower-colour loads are

\[
                        1^{8d+8}2^{16},                     \tag{0.4}
\]

while its upper-colour loads are

\[
                        2^8(d+3)^8.                         \tag{0.5}
\]

Hence the mandatory bank violates the lower partition matroid, the upper
partition matroid, middle cap two, and the graphic matroid before a residual
selector is chosen.  Jointly reselecting the ambient forest cannot repair a
forced-set dependence.  The known frozen-`m=9` post-hoc failure is therefore
strictly weaker than this obstruction.

The sharpest local witness is already one packet: its `8d+22` consecutive
Johnson edges use only fourteen upper colours, with load profile

\[
                         1^6(d+2)^8.                         \tag{0.6}
\]

Two consecutive coatom edges in the first block are distinct but have the
same union.  Thus no upper-exact Catalan forest can contain even one complete
literal packet path.

## 1. Authentication of the source relation

Let `G_(pi,e)` be the guarded relabelled block

\[
 G_{\pi,e}=\pi\{a_0,a_1\}\mid\pi Q_d^e
               \mid\pi\{a_1,a_2\}.
\]

The two words are

\[
\begin{aligned}
 {\cal W}^-&=G_{1,0}G_{\beta,1}G_{\alpha,1}G_{\alpha\beta,0},\\
 {\cal W}^+&=G_{1,1}G_{\beta,0}G_{\alpha,0}G_{\alpha\beta,1}.
\end{aligned}                                                \tag{1.1}
\]

For one addressed interval value `X`, write

\[
 \chi[X]=(1-\alpha)(1-\beta)[X].                            \tag{1.2}
\]

The explicit sharp-source classification shows that `chi[X]` can be
nonzero only when the active part contains exactly one label from each of
`{a0,a2}` and `{a1,a3}`.  At every such address the two phase values agree.
Therefore the four signed block contributions in (1.1) cancel
coefficientwise.

At each of the three seams, the literal suffix--prefix union is the same in
the two words at every pair of relative lengths.  An interval crossing two
seams contains a complete block and therefore sees the common total union.
The complete macro prefixes and suffixes are also pointwise equal.  Hence,
for arbitrary fixed exterior words `X,Z`,

\[
 \operatorname{Deck}_q(X{\cal W}^-Z)
   =\operatorname{Deck}_q(X{\cal W}^+Z)\qquad(q\ge1).        \tag{1.3}
\]

Moreover `alpha g_8=beta g_8=-g_8` and
`alpha beta g_8=g_8`; the signed phase pattern gives

\[
            g_8-\beta g_8-\alpha g_8+\alpha\beta g_8=4g_8. \tag{1.4}
\]

Equations (1.3)--(1.4) authenticate the source action while making no owner
embedding claim.

## 2. Exact forced-row obstruction

An exact Catalan selector on rank-`r` owners chooses Boolean diamonds so
that their lower and upper colours are each injective, every middle owner
has degree at most two, and the physical Johnson graph is acyclic.  These
are respectively two partition rows, a capacity row, and a graphic row.

Let `P` be the support of either literal four-block endpoint after duplicate
edges are suppressed.  Equations (0.3)--(0.5) give four independent
certificates.

1. Sixteen lower partition classes contain two forced edges.
2. Every one of the sixteen upper partition classes is overloaded: eight
   have load two and eight have load `d+3`.
3. Sixteen owners have forced degree three and eight have degree four.
4. Since the forced graph is connected,
   \[
                  |P|-r_{\rm gr}(P)=17.                     \tag{2.1}
   \]

Thus `P` is dependent in every relevant selector row.  In particular,
contraction by `P` is not a legitimate way to formulate a residual matroid
intersection: a forced seed must first be independent in every contracted
matroid.

At the exact `m=9,d=6` calibration, (0.2)--(0.5) become

\[
 284\text{ owner occurrences on }72\text{ owners},\quad
 88\text{ distinct edges},\quad
 |\operatorname{supp}L|=72,\quad
 |\operatorname{supp}U|=16,                                \tag{2.2}
\]

with degree histogram `2^48 3^16 4^8` and graphic nullity seventeen.
These are properties of the prescribed four packets, not properties of the
previously selected rotation forest.

Exact `d`-letter overlaps at the three source joins do not identify the
width-`d+1` owner windows.  Even the largest phase-common literal overlap
misses six required owner occurrences and creates fourteen nonrequired
ones in either phase; a smaller common collar cannot restore a missing
union by monotonicity.

## 3. Why uniform private tags do not strictize the relation

For every addressed surplus value, join the block contributing it
positively to the block contributing the cancelling negative occurrence.
The sparse rows force precisely

\[
                 0-1,\quad0-2,\quad3-1,\quad3-2,            \tag{3.1}
\]

the connected graph `K_(2,2)`.

Suppose a uniform tag set `Z_i` is adjoined to every source letter in block
`i`.  A cancellation across `i-j` in (3.1) remains a literal equality only
if `Z_i=Z_j`.  Connectivity forces all four tag sets equal.  Equal tags do
not separate the repeated owners or palette values; distinct private tags
destroy (1.3).  This closes the simplest disjointization escape.

Position-dependent tags, a quotient weave which identifies occurrences,
or a different upper-rainbow owner realization are not excluded.

## 4. Exact common-completion theorem for a future strictized pair

The appropriate selector theorem becomes available only after replacing the
literal packets by two genuinely legal phase banks `P^0,P^1`.  Assume:

* each `P^epsilon` is a cap-two Johnson linear forest;
* its lower and upper labels are injective;
* the two phases use the same lower-label set and the same upper-label set.

Delete those palette classes from the Boolean-diamond catalogue, and let
`E_0` be the residual candidate set.  A common residual set `R subset E_0`
completes both phases to exact Catalan forests if and only if all three rows
hold:

1. `R` is a perfect matching of the residual lower--upper diamond graph;
2. for every middle owner `v`,
   \[
       d_R(v)\le 2-\max_{\epsilon\in\{0,1\}}d_{P^\epsilon}(v); \tag{4.1}
   \]
3. `R` is independent in both contracted graphic matroids
   \[
       M(J(2m,m))/P^0,\qquad M(J(2m,m))/P^1.             \tag{4.2}
   \]

Necessity is immediate from palette exactness, cap two, and forest
independence.  Conversely, row 1 fills every omitted lower and upper class
once, row 2 gives the degree cap in both phases, and row 3 says exactly that
neither completed physical graph contains a cycle.  This proves
sufficiency.

On the face where palette completion and cap (4.1) are automatic, (4.2) is
ordinary two-matroid intersection.  A common residual independent set of
size `s` exists exactly when Edmonds' inequality

\[
 r_{M_0}(A)+r_{M_1}(E_0\setminus A)\ge s
                    \qquad(A\subseteq E_0)                 \tag{4.3}
\]

holds.  If the two packet phases induce the same component partition, the
two graphic contractions coincide; one remaining partition row then gives
ordinary partition--graphic matroid intersection.

The unrestricted selector has two palette partition rows, two graphic rows,
and the middle-cap correlation.  It is not ordinary two-matroid
intersection.  In fact, cap-two linear forests do not form a matroid: both

\[
 I=\{12,23,34\},\qquad J=\{25,53,31,14\}                   \tag{4.4}
\]

are linear forests and `|I|<|J|`, but no edge of `J-I` augments `I` without
creating degree three or a cycle.

Finally, an exact Catalan forest always has `Cat_m` total components by
Euler's identity.  “Bounded components” can therefore mean only that the
protected packet footprint meets a bounded number of those components, or
that a later tagged connector contracts them to bounded boundary state; it
cannot mean that the exact central forest itself has `O(1)` components.

## 5. Sharp remaining target

The current four-block relation should be retained as an exact source and
compiler-language identity, but not used as a physical CBC endpoint.  A
live physical route must provide one of the following before any residual
selector is run:

1. a nonliteral quotient weave which realizes one simple copy of the
   repeated owner/palette bank while retaining the `K_(2,2)` occurrence
   pairing;
2. a new upper-rainbow tensor replacing the constant-union coatom blocks;
3. a sparse realization containing only the changing octagon `C8` atoms,
   with the remaining source relation carried by a separate rank-correct
   rail.

Any candidate must first pass forced-set independence in both palette
partitions, cap two, and the graphic row.  Only then does Theorem 4 reduce
the joint completion to a meaningful residual selector problem.

## 6. Replays and scope

The source relation/action replay, the literal physical no-go, and an
independent all-relabel/m9 audit are respectively:

```text
scratch/audit_h2_c8_four_relabelled_graded_or_action_20260801.py
scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py
scratch/audit_catalan_m9_four_relabelled_octagon_joint_selector_obstruction_20260801.py
```

They check the source identity and `4g_8` action, the all-`d` owner/palette
formulas and overlap gate, and all ten direct-sum relabelling hits with the
literal `m=9` calibration.  The third replay also confirms the intrinsic
single-packet repeated-upper witness.

Proved: exact source action; exact literal selector no-go; exact conditional
common-completion criterion after a future strictization.

Not proved: a quotient weave, a strict-upper replacement packet, a bounded
physical compiler boundary, or `nu(k)<=B(k)+O(1)`.
