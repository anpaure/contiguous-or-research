# The canonical MSW upper-`q2` missing language is a one-counter chamber language

**Date:** 2026-08-05  
**Method:** exact `Gamma` inverse criterion; no computation or finite search  
**Status:** unconditional classification of the canonical MSW upper-`q2`
image, including the two endpoint flaw classes.  It also proves that a
finite collection of fixed prefix macros, closed only under the known Dyck
suffix tensor, cannot cover all canonical holes.

## 0. Outcome

Let `T` be a binary path of length `2r` ending at height four.  Mark as
barriers the down-steps of `T` starting at height two or three.  Between two
successive barriers, every possible inverse pair in the exact MSW `Gamma`
criterion lies in one **productive chamber**.  Such a chamber has a unique
central passage

```text
                              U_1 U_2,
```

with an arbitrary low renewal before it and an arbitrary high renewal after
it.

If the chamber contains `a` up-steps starting at height zero and `b`
up-steps starting at height three, put

```text
A = number of U_0 steps strictly before the chamber,
B = number of U_3 steps strictly after the chamber.
```

Then the left and right ordinal labels in the exact inverse criterion are
the two integer intervals

\[
                         I=[A,A+a],\qquad J=[B,B+b].              \tag{0.1}
\]

Every `j in I intersect J` gives one and only one pair satisfying the four
height, corridor, and ordinal conditions.  It is a canonical internal
upper-`q2` occurrence precisely when the balanced predecessor obtained by
flipping those two up-steps down lies in a Chung--Feller flaw class
`1,...,r-1`.

The two excluded endpoint classes are completely explicit decorations:

* a flaw-zero predecessor can occur only for a type-`(1,3)` pair;
* a flaw-`r` predecessor can occur only for a type-`(0,2)` pair.

There is at most one pair of each type for a fixed target.  Thus the raw
interval test differs from the canonical internal test by at most two named
labels.

Chronologically, the intervals `I` move weakly to the right and the
intervals `J` move weakly to the left.  Hence, apart from the at most two
endpoint-decorated coincidences, a missing word has one cut:

```text
all early productive chambers:   max I < min J,
all late productive chambers:    max J < min I.
```

This is an exact one-counter renewal grammar.  It is not a finite-state
language.  On the regular slice

\[
 T_{a,b}=(1100)^a\,111\,(10)^b\,1,\qquad a,b\ge2,               \tag{0.2}
\]

one has

\[
              T_{a,b}\text{ is missing}\quad\Longleftrightarrow
              \quad a>b+1.                                    \tag{0.3}
\]

Every word in the missing half of (0.2) is irreducible under removal of a
height-four Dyck suffix.  Consequently the complete missing language has
infinitely many suffix-irreducible prefix cores.  In particular, finitely
many fixed prefix packets, even after tensoring each with every Dyck suffix,
cannot repair all canonical holes.

The exact two-hex packet in
`MATH_THEOREM_MSW_TWO_HEX_T0V_HOLE_RELAY_AND_DYCK_TENSOR_20260805.md`
repairs one full cylinder of this grammar,

\[
                    T_0\mathcal D,
 \qquad T_0=(1100)^2 1111,                                    \tag{0.4}
\]

where `mathcal D` is the Dyck language.  A complete repair theorem still
needs a **counter-carry macro** transporting that relay through arbitrary
low renewals.  The chamber theorem shows exactly what the transported state
must be: one signed ordinal gap and one of finitely many endpoint
decorations.

## 1. The exact inverse criterion

For an up-step position `p`, let `H_T(p)` be its starting height.  The exact
MSW inverse theorem says that `T` has an internal canonical upper-`q2`
occurrence if and only if there are up-step positions `p<q` such that

\[
\begin{array}{ll}
\text{(a)}&H_T(p)\in\{0,1\},\\
\text{(b)}&H_T(q)\in\{2,3\},\\
\text{(c)}&\text{no down-step starting at height two or three lies
strictly between `p` and `q`,}\\
\text{(d)}&U_0(T;[1,p))=U_3(T;(q,2r]),
\end{array}                                                     \tag{1.1}
\]

and the balanced path `T-{p,q}` lies in one of the internal flaw classes
`1,...,r-1`.  This is Lemma 3.1 of
`MATH_THEOREM_MSW_Q1_INVERSE_AND_SQRT_BOUND_20260725.md`.

Call a down-step beginning at height two or three a **barrier**.  A chamber
is a maximal open interval of positions between consecutive barriers,
allowing the initial and terminal intervals.  Condition (1.1c) says exactly
that `p,q` lie in one common chamber.

## 2. Geometry of one productive chamber

A chamber is productive if it contains an up-step from height zero or one
and a later up-step from height two or three.

### Lemma 2.1 (unique bridge)

Every productive chamber contains one unique consecutive pair `U_1U_2`.
Before this pair the path stays at height at most one; after it the path
stays at height at least three.

#### Proof

To pass from the low candidate band `{0,1}` to the high candidate band
`{2,3}`, the path must use `U_1` and then `U_2`.  Once `U_1` has reached
height two, returning to height one requires a `D_2`, which is a barrier.
Thus there is at most one `U_1` in the chamber after which a high candidate
can occur.  At height two, the next step is either `U_2` or the barrier
`D_2`; productivity forces `U_2`.  Once at height three, returning to
height two requires the barrier `D_3`.  This proves uniqueness and the two
height restrictions.  \(\square\)

Let `C` be a productive chamber.  Put

\[
\begin{aligned}
 A_C&=U_0(T;\text{positions strictly before }C),\\
 a_C&=U_0(T;C),\\
 B_C&=U_3(T;\text{positions strictly after }C),\\
 b_C&=U_3(T;C).
\end{aligned}                                                   \tag{2.1}
\]

### Lemma 2.2 (interval labels)

The values of the left side of (1.1d), over all eligible `p` in `C`, are

\[
                         I_C=[A_C,A_C+a_C]\cap\mathbb Z.         \tag{2.2}
\]

The values of the right side, over all eligible `q` in `C`, are

\[
                         J_C=[B_C,B_C+b_C]\cap\mathbb Z.         \tag{2.3}
\]

Every label in either interval is carried by a unique eligible step.

#### Proof

Before the unique `U_1`, successive `U_0` steps have labels

\[
              A_C,A_C+1,\ldots,A_C+a_C-1.
\]

The final `U_1` has label `A_C+a_C`, proving (2.2).  Dually, the unique
`U_2` has all `b_C` chamber `U_3` steps and all later `U_3` steps to its
right, so its label is `B_C+b_C`.  Reading the chamber `U_3` steps from
left to right gives the remaining labels

\[
              B_C+b_C-1,\ldots,B_C.
\]

This proves (2.3) and uniqueness.  \(\square\)

For `j in I_C`, let `p_C(j)` be its unique low step.  For `j in J_C`, let
`q_C(j)` be its unique high step.  Define the endpoint-exception set

\[
 \mathcal E_C(T)=
 \left\{j\in I_C\cap J_C:
   \operatorname {fl}\bigl(T-\{p_C(j),q_C(j)\}\bigr)\in\{0,r\}
 \right\},                                                     \tag{2.4}
\]

where `fl` is the Chung--Feller flaw number.

### Theorem 2.3 (exact chamber classification)

\[
 \boxed{
 T\in\operatorname {im}\Gamma_{\rm internal}
 \iff
 \text{some productive chamber `C` has }
 (I_C\cap J_C)\setminus\mathcal E_C(T)\ne\varnothing.}         \tag{2.5}
\]

Consequently

\[
 \boxed{
 T\text{ is canonically missing}
 \iff
 I_C\cap J_C\subseteq\mathcal E_C(T)
 \text{ for every productive chamber `C`.}}                    \tag{2.6}
\]

#### Proof

By Lemma 2.1, condition (1.1c) is equivalent to placing both steps in one
productive chamber.  Conditions (1.1a)--(1.1b) select precisely the steps
listed in Lemma 2.2.  Condition (1.1d) is equality of their unique integer
labels, hence membership in `I_C intersect J_C`.  Finally (2.4) removes
exactly the two endpoint flaw classes excluded from the domain of the
internal turn map.  Every implication is reversible.  \(\square\)

### Lemma 2.4 (endpoint scope)

Across all chambers, `mathcal E_C(T)` contains at most two labels.  A
flaw-zero exception is necessarily of height type `(1,3)`; a flaw-`r`
exception is necessarily of height type `(0,2)`.

#### Proof

If `x=T-{p,q}` is Dyck, then the changed down-step at `p` must start at
positive height in `x`, forcing `H_T(p)=1`; after the first height shift,
the changed down-step at `q` must also start at positive height, forcing
`H_T(q)=3`.  Thus the pair has type `(1,3)`.  If `x` is in the terminal
all-negative Chung--Feller class, the reflected argument forces type
`(0,2)`.

Lemma 9.1 of the exact inverse theorem proves that a fixed target has at
most one occurrence of each of the types `(1,3)` and `(0,2)`.  Therefore
there are at most two endpoint exceptions in total.  \(\square\)

## 3. The monotone one-counter grammar

List the productive chambers in chronological order as
`C_1,...,C_s`.  Put `I_i=I_(C_i)` and `J_i=J_(C_i)`.

### Lemma 3.1 (opposite monotonicity)

For `i<j`,

\[
             \max I_i\le\min I_j,
             \qquad
             \max J_j\le\min J_i.                              \tag{3.1}
\]

#### Proof

Every `U_0` in `C_i` occurs before `C_j`, so the prefix counter at the
start of `C_j` is at least the prefix counter at the end of `C_i`.  This
is the first inequality.  Every `U_3` in `C_j` lies to the right of
`C_i`, so the suffix counter before `C_i` includes the complete `C_j`
contribution.  This is the second inequality.  \(\square\)

For a chamber with disjoint intervals, call it **under** when

\[
                         \max I_i<\min J_i,                       \tag{3.2}
\]

and **over** when

\[
                         \max J_i<\min I_i.                       \tag{3.3}
\]

### Corollary 3.2 (one-cut theorem)

Among the chambers with disjoint intervals, every under chamber precedes
every over chamber.  Hence there is a unique cut, allowing either side to
be empty.

#### Proof

If `C_i` is over, then (3.1) implies for every `j>i`

\[
                 \max J_j\le\min J_i<\max J_i<\min I_i
                    \le\min I_j,
\]

so `C_j` is over.  The under statement follows by reversing time.  \(\square\)

An equivalent scalar state is

\[
                         z_i=A_{C_i}-B_{C_i}.                     \tag{3.4}
\]

The chamber is raw-covered exactly when

\[
                         -a_{C_i}\le z_i\le b_{C_i}.             \tag{3.5}
\]

As `i` increases, `z_i` is nondecreasing.  Low excursions below height
one and high excursions above height three are ordinary Catalan renewal
blocks; barriers give only finitely many band-transition types.  Therefore
(3.4)--(3.5), together with the at most two endpoint flags of Lemma 2.4,
is an exact deterministic one-counter renewal grammar for the complete
canonical missing language.

## 4. The language is not finite-state

Take (0.2).  Every copy of `1100` ends with a barrier `D_2`, so none of its
chambers is productive.  The final chamber contains the central
`U_0U_1U_2`, followed by the `b` loops `U_3D_4` and the terminal `U_3`.
Its intervals are

\[
                         I=\{a,a+1\},
 \qquad                 J=[0,b+1]\cap\mathbb Z.                 \tag{4.1}
\]

If `a>b+1`, they are disjoint, so Theorem 2.3 proves that the target is
missing.  If `a<=b`, pair the central `U_0` with the unique `U_3` having
exactly `a` later `U_3` steps.  If `a=b+1`, pair the same `U_0` with the
central `U_2`.  In both cases (1.1) holds.  For `a,b>=2`, the resulting
balanced predecessor visits both positive and negative heights, so it is
neither endpoint flaw class.  This proves (0.3).

Under the block coding

```text
A -> 1100,    C -> 111,    B -> 10,    D -> 1,
```

the intersection of the missing language with the regular slice
`A^(>=2) C B^(>=2) D` pulls back to

\[
                  \{A^aCB^bD:a>b+1,\ a,b\ge2\}.                 \tag{4.2}
\]

This is not regular, by the pumping lemma or Myhill--Nerode.  Regular
languages are closed under intersection and inverse homomorphism, so the
canonical missing language is not regular.

Moreover, after the central word `111`, every nonterminal visit to height
four in (0.2) is immediately followed by `D_4` and returns to height three.
Thus no word in (0.2) has a nonempty suffix which is Dyck when read from
height four.  The missing half of (0.2) supplies infinitely many
Dyck-suffix-irreducible prefix cores.

## 5. Exact implication for repair macros

Call a **fixed suffix-tensor packet** a fixed finite prefix incidence
exchange which remains valid after appending an arbitrary height-four Dyck
suffix.  A finite collection of such packets repairs a finite union of
cylinders

\[
                         P_1\mathcal D\cup\cdots\cup P_t\mathcal D. \tag{5.1}
\]

The suffix-irreducible family in Section 4 meets (5.1) in at most the
finite set of prefixes `P_1,...,P_t`.  Therefore:

### Corollary 5.1

No finite collection of fixed suffix-tensor packets covers the complete
canonical MSW upper-`q2` missing language.

This statement is deliberately scoped.  It does not rule out finitely many
**recursive packet schemas** carrying the unbounded counter `z`.

The frozen two-hex packet for `T_0` proves that one complete cylinder is
repairable.  Its two hexagons preserve every old q2 target, and packets for
distinct suffixes are support-disjoint.  In the grammar above, `T_0` is the
minimal over chamber

\[
                         I=\{2,3\},\qquad J=\{0,1\}.             \tag{5.2}
\]

Thus the precise next statement is a renewal conjugacy:

> **Counter-carry macro.**  Given a repair relay at signed chamber gap
> `z`, transport it through one low or high Catalan renewal, obtaining the
> relay at the updated gap, while preserving all old q2 multiplicities,
> the component-merging topology, and the untouched suffix stem.

Repeated counter-carry, followed by the frozen `T_0` relay at the terminal
minimal chamber, would give one uniform recursive schema for all chambers
generated by (3.4)--(3.5).  This conjugacy is not proved here.

## 6. Scope

The theorem classifies the canonical upper-`q2` language only.  It neither
constructs the counter-carry packet nor proves that packets belonging to
different non-suffix contexts have disjoint physical supports.  It makes
no claim about arbitrary-width upper rows, residence, lower compilation,
or a `B(k)+O(1)` word.

