# Iterated \(s_1\)-component routing: exact first split and hereditary obstruction

## 0. Decision

Let

\[
 d=\operatorname{Cat}_r=\theta p,
 \qquad4\le\theta<16,
\]

and compare the canonical anchored MSW local factor with its coordinate
translate by \(s_1=(2\,3)\).  The claimed component law is exact:

\[
 k_j=\operatorname{Cat}_j+\operatorname{Cat}_{j+1},
 \qquad
 n_j=\operatorname{Cat}_{r-j-2},\qquad0\le j\le r-2.     \tag{0.1}
\]

The bounded-\(j\) components carry

\[
                         \left(\frac38+o(1)\right)d      \tag{0.2}
\]

rows, while their complement carries \((5/8+o(1))d\).
Switching an arbitrary union of these components is a literal integral
anchored factor, so the first \(3/8\)--\(5/8\) split is exact and
port-legal.

The proposed bounded-depth routing tree does **not** follow.  There are
three independent obstructions.

1. The component law (0.1) is a law for the canonical comparison
   \(F_{\rm MSW}\) versus \(s_1F_{\rm MSW}\); it is not hereditary after a
   partial component switch.
2. Component partitions for distinct legal local target coordinates are
   not laminar.  Already for \(r=3\), the \(s_1=(2\,3)\) and
   \(s_2=(4\,5)\) partitions cross in all four possible intersections.
   Thus a second component switch cannot act inside one first-generation
   target packet.
3. Exact middle ownership and port anchoring do not make the lower-shadow
   profiles additive.  A window meeting two routing levels couples their
   choices, so the six-level construction is one joint atom unless an
   additional full-profile product theorem is proved.

There is also a purely numerical correction: a complete ideal binary
\(5/8\)--\(3/8\) recursion starting from mass \(16p\) has 21 terminal
leaves of mass at most \(p\), not at most 16.  Merging those leaves into
16 target coordinates is a separate bin-packing and exact-ledger problem.

Hence the current component theorem proves one legal macroscopic split,
not an iterated Catalan router.  Uniform final fibre size at most \(p\)
remains unproved.

## 1. Exact component ledger

For a Dyck suffix \(R\in D_{r-j-2}\), the \(s_1\)-component root block is

\[
 \mathcal C_{j,R}
 =\{AR:A\in\mathcal A_j\},                              \tag{1.1}
\]

where

\[
 \mathcal A_j=
 \{1u0:u\in D_{j+1}\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in D_j\}.                                 \tag{1.2}
\]

Therefore

\[
 |\mathcal C_{j,R}|
 =\operatorname{Cat}_{j+1}+\operatorname{Cat}_j=k_j,
\]

and there are \(n_j=\operatorname{Cat}_{r-j-2}\) such blocks.  The exact
convolution

\[
 \sum_{j=0}^{r-2}k_jn_j=\operatorname{Cat}_r=d          \tag{1.3}
\]

checks that they partition all ports.

For fixed \(j\), the Catalan quotient gives

\[
 \frac{\operatorname{Cat}_{r-j-2}}{\operatorname{Cat}_r}
 \longrightarrow4^{-j-2}.                              \tag{1.4}
\]

If \(J=J(r)\to\infty\) sufficiently slowly, then uniformly for \(j\le J\),
(1.4) may be summed and \(k_J=o(p)\).  Hence every selected component has
fewer than \(p\) rows and

\[
\begin{aligned}
 \frac1d\sum_{j\le J}k_jn_j
 &\longrightarrow
 \sum_{j\ge0}\frac{\operatorname{Cat}_j+\operatorname{Cat}_{j+1}}
                       {4^{j+2}}\\
 &=\frac18+\frac14=\frac38.                            \tag{1.5}
\end{aligned}
\]

The corresponding number of components is

\[
 \sum_{j\le J}n_j
 =\left(\frac1{12}+o(1)\right)d
 =\left(\frac\theta{12}+o(1)\right)p.                  \tag{1.6}
\]

This resolves an ambiguity in the phrase “selectable at most \(p\)
components.”

* If it means **components of size at most \(p\)**, then (1.5) is correct.
* If it means **a collection containing at most \(p\) components**, then
  (1.5) is correct only for \(\theta\le12+o(1)\).

For \(12<\theta<16\), the canonical small-\(j\) family contains more than
\(p\) components.  The best \(p\)-component subfamily of this tail is
obtained by discarding the required number of size-two \(j=0\) components.
The discarded count is

\[
 d\left(\frac1{12}-\frac1\theta+o(1)\right),
\]

which is smaller than the available \(d/16+o(d)\) size-two count.  Its
remaining row mass is

\[
 \boxed{
 \left(\frac5{24}+\frac2\theta+o(1)\right)d,}           \tag{1.7}
\]

decreasing from \(3d/8\) at \(\theta=12\) to \(d/3\) as
\(\theta\uparrow16\).  Other upper-end components may be added, but that is
no longer the claimed canonical \(3/8\) tail.

## 2. What composes exactly

Let \(F\) be any anchored \(D_r\)-port-transversal factor and let
\(\sigma\) be a coordinate permutation preserving \(D_r\).  Reindex
\(\sigma F\) by the inherited ports, so its row labelled \(P\) has endpoints
\(P\) and \([2r]\setminus P\).  Overlay \(F\) and \(\sigma F\) by ownership
of all \(X\)-states and all adjacent-union \(Y\)-colours.

Every connected overlay component carries the same root-label set on its
two shores.  Choosing either complete shore on every component therefore
preserves

1. every \(X\)-owner exactly once;
2. every \(Y\)-owner exactly once; and
3. one path with endpoints \(P,[2r]\setminus P\) for every \(P\in D_r\).

Thus an arbitrary component choice is an exact anchored factor.  This
argument may be repeated: after obtaining \(F_1\), compare \(F_1\) with
\(\sigma_2F_1\), recompute the complete ownership overlay, and switch whole
components.  Inductively, every intermediate factor is integral, exact,
and port-legal.

This is the full positive composability statement.  It does **not** say
that the new components refine the target packets created earlier, or
that they retain the sizes (0.1).

## 3. Minimal nonlaminar obstruction

The failure occurs already on the five Dyck roots of \(D_3\).  Use

\[
\begin{aligned}
T_1&=111000,&T_2&=110100,&T_3&=110010,\\
T_4&=101010,&T_5&=101100.
\end{aligned}                                           \tag{3.1}
\]

Formula (1.1) gives the two \(s_1=(2\,3)\) component blocks

\[
 B_0=\{T_3,T_4\},
 \qquad
 B_1=\{T_1,T_2,T_5\}.                                  \tag{3.2}
\]

Let \(\mu(w)=\overline{\operatorname{rev}(w)}\).  Path reversal carries
the \(s_1\) comparison to the \(s_2=(4\,5)\) comparison, and

\[
 \mu(T_1)=T_1,\quad\mu(T_2)=T_2,\quad
 \mu(T_3)=T_5,\quad\mu(T_4)=T_4.                         \tag{3.3}
\]

Hence the \(s_2\)-component blocks are

\[
 C_0=\{T_4,T_5\},
 \qquad
 C_1=\{T_1,T_2,T_3\}.                                  \tag{3.4}
\]

Their intersection table is

\[
\begin{array}{c|cc}
 &C_0&C_1\\ \hline
B_0&\{T_4\}&\{T_3\}\\
B_1&\{T_5\}&\{T_1,T_2\}.
\end{array}                                             \tag{3.5}
\]

Every cell is nonempty.  In particular no nontrivial \(s_2\)-component is
contained in either \(s_1\)-component.  If the first switch sends \(B_0\)
to one target coordinate and leaves \(B_1\) at another, then either second
component choice necessarily contains ports bearing both first-generation
target labels.

This refutes the laminar routing-tree assertion.  Distinct local target
coordinates do not cure it: they label the crossed cells, but the legal
move remains a whole component containing several labels.

The same problem appears structurally in (1.2).  A block
\(\mathcal A_jR\) is a union of two different first-return families of
sizes \(\operatorname{Cat}_{j+1}\) and \(\operatorname{Cat}_j\).  It is not
itself a complete context fibre \(C[D_t]\).  Therefore the local
port-substitution theorem cannot simply be invoked recursively inside one
\(s_1\)-component.

## 4. The ideal size recursion does not give sixteen packets

Ignore the preceding legality problem and suppose every packet of mass
\(x\) can be split exactly into masses \(5x/8\) and \(3x/8\).  Since

\[
 16\left(\frac58\right)^6
 =\frac{15625}{16384}<1,                               \tag{4.1}
\]

six levels do force every leaf below \(p\) when the initial mass is below
\(16p\).

They do not force at most sixteen leaves.  Let \(L(x)\) be the number of
terminal leaves obtained by recursively splitting every node larger than
one:

\[
 L(x)=1\quad(x\le1),
 \qquad
 L(x)=L(5x/8)+L(3x/8)\quad(x>1).                        \tag{4.2}
\]

Direct substitution gives

\[
\begin{aligned}
L(16)&=L(10)+L(6)=13+8=21,\\
L(10)&=L(25/4)+L(15/4)=8+5,\\
L(6)&=L(15/4)+L(9/4)=5+3.
\end{aligned}                                           \tag{4.3}
\]

None of the intermediate arguments in this evaluation equals one, so the
same value 21 persists for all initial masses sufficiently close to
\(16p\).

The inequality \(d<16p\) says only that some abstract partition into at
most sixteen \(p\)-sized bins is possible.  It does not say that the leaves
of the fixed \(5/8\)--\(3/8\) recursion admit such a binning, still less
that several leaves can be assigned the same target while preserving both
ownership ledgers and the cap at every depth.

## 5. Full-profile collateral

At one distinguished child window, switching a component can replace a
common parent target coordinate by its transposed coordinate.  A complete
row substitution also changes every lower window whose boundary cuts an
affected phase slab.  After two routing levels, a window may meet both
slabs; its target is then a joint function of both component choices.

Consequently a six-level construction within one parent is not a product
of six independent binary atoms.  Its exact atom is the connected overlap
closure of all substitutions met by one serviced window.  The full
histogram has the form

\[
 \mu_q=\lambda_q+\sum_Au_{A,G_A,q}                      \tag{5.1}
\]

only after all overlapping routing levels have been grouped into joint
atoms \(A\).  If the six levels lie in one parent, that closure may contain
the entire \(d\)-row fibre.

This matters twice.

1. The same joint choice must work at every protected depth; one cannot
   choose the \(3/8\) shore separately for each \(q\).
2. The distinguished target split does not bound positive collateral.
   PCap descent requires the full weighted target inequality, and integral
   selection additionally requires a square-fragmentation bound for every
   joint atom.

Neither property follows from (0.1), port anchoring, or the use of distinct
coordinate pairs.  Component switches preserve the two middle-ownership
ledgers, but those ledgers contain no lower-shadow sign information.

## 6. Exact theorem that would repair the route

A valid bounded-depth router would need a hereditary strengthening of the
canonical component law.  One sufficient statement is the following.

For every current target packet \(B\subseteq D_r\) of size greater than
\(p\), construct a coordinate automorphism \(\sigma_B\) and a union of
complete components in the overlay of the **current** factor with
\(\sigma_B\) times that factor such that

1. every selected component has its root block contained in \(B\);
2. the selected root mass lies between \((3/8-o(1))|B|\) and
   \((3/8+o(1))|B|\);
3. all crossing-window profiles have atomwise target multiplicity \(O(p)\);
4. choices for different packets are jointly exact and influence-disjoint,
   or are supplied with one joint-library proof; and
5. the same choices satisfy the weighted PCap inequality at every serviced
   depth.

Condition 1 is already false for the naive succession \(s_1,s_2\) by
(3.5).  Conditions 3--5 are the full-profile collateral gate.

Without such a theorem, the exact \(3/8\) first split cannot be iterated.
The refined observation \(d<16p\) reduces the desired number of final
packets to a constant, but it does not supply the missing hereditary
component refinement.

## 7. Final verdict

The \(s_1\) overlay hierarchy gives one strong and completely legal move:
it can reroute a \(3/8+o(1)\) portion of the canonical fibre through
bounded-size anchored components.  Arbitrary subsequent component switches
remain exact and port-legal **after recomputation**.

What fails is the routing-tree interpretation.  The recomputed components
are not known to retain Catalan sizes, and distinct coordinate component
partitions cross even in the five-root base case.  Moreover their lower
profiles form joint atoms rather than independent target-coordinate
channels.  Thus neither a six-level \(5/8\)--\(3/8\) decomposition nor a
uniform final cap \(p\) has been proved.  The obstruction is component
overlap plus uncontrolled full-profile collateral, not port legality of an
individual switch.
