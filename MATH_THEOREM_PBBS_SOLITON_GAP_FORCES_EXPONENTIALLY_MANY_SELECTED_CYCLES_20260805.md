# A soliton gap forces whole PBBS cycles into every max-height section

**Date:** 2026-08-05  
**Method:** peak-pruning algebra plus the exact periodic-BBS action--angle
formula; no state search  
**Status:** unconditional subject only to the standard exact periodic-BBS
action--angle correspondence already used in the repository's component
census.  The theorem disproves the hoped-for statement that only `O(1)`
PBBS components are wholly selected.  In fact there are exponentially many
on an infinite sequence of dimensions.

## 1. Peak-pruning partition

For a Dyck word `D`, let

\[
 a_s(D)=\operatorname {pk}(\partial^{s-1}D),
 \qquad s\ge1,
\tag{1.1}
\]

where `partial` deletes every peak simultaneously.  Write `lambda(D)` for
the partition conjugate to the nonincreasing profile `(a_s)`, so

\[
 \lambda_j(D)=\max\{s:a_s(D)\ge j\}.
\tag{1.2}
\]

The exact PBBS peak-pruning theorem gives:

1. `lambda(D)` is invariant under the rooted PBBS evolution;
2. `a(PQ)=a(P)+a(Q)` for Dyck words `P,Q`;
3. if `E` is Dyck of height `h`, then

   \[
                        a(1E0)=a(E)+e_{h+1}.
   \tag{1.3}
   \]

In particular

\[
 \lambda_1(D)=\operatorname {ht}(D),
 \qquad
 \lambda_2(D)=\max\{s:a_s(D)\ge2\}.
\tag{1.4}
\]

## 2. Spectral-gap forcing theorem

### Theorem 2.1

Let `C` be a PBBS `g=f^2` component with soliton partition

\[
                  \lambda=(\lambda_1,\lambda_2,\ldots),
\]

where missing parts are zero.  If

\[
                         \lambda_1-\lambda_2\ge2,
\tag{2.1}
\]

then **every** outgoing q1 occurrence on `C` is the unique max-height
occurrence of its q1 colour.  Consequently every max-height q1 section,
independently of all tie decisions, contains the whole component `C`.

#### Proof

Take an arbitrary rooted phase `A=0_rD` of `C`, put

\[
 H=\operatorname {ht}(D)=\lambda_1,
\]

and let `C_j` be the first primitive factor of `D` having height `H`.
The outgoing-occurrence criterion in
`MATH_THEOREM_PBBS_OUTGOING_MAX_HEIGHT_OCCURRENCE_CRITERION_20260805.md`
says that the three competing deficit-three block heights are

\[
                         H-1,quad H_{tail}-1,quad H_{later}.
\tag{2.2}
\]

We show that the last two are at most `H-2`.

There cannot be two primitive factors of height `H`: by additivity (1.3),
each would contribute at least one unit to `a_H(D)`, forcing
`a_H(D)>=2` and hence `lambda_2>=H`, contrary to (2.1).

Write the unique height-`H` factor as `1E0`.  The first child factor of
`E` which reaches height `H-1` contains the first global maximum.  The
tail measured by `H_tail` is the concatenation of the later child factors.
If `H_tail=H`, one of those later child factors also has height `H-1`.
Additivity would then give `a_(H-1)(E)>=2`, and therefore
`lambda_2(D)>=H-1`, again contradicting (2.1).  Hence

\[
                         H_{tail}\le H-1.
\tag{2.3}
\]

Finally, if a later primitive factor of `D` had height at least `H-1`, it
would contribute one unit to `a_(H-1)(D)`, while the height-`H` factor
already contributes another.  This too would force
`lambda_2>=H-1`.  Therefore

\[
                         H_{later}\le H-2.
\tag{2.4}
\]

Equations (2.3)--(2.4) are exactly the unique-max conditions of the
outgoing-occurrence criterion.  The phase was arbitrary, and the soliton
partition is constant on the whole PBBS component, proving the theorem.
`square`

### Scope warning

Condition (2.1) is sufficient.  This theorem does not claim its converse:
when `lambda_2>=lambda_1-1`, whether every phase is selected may depend on
the action/angle orbit, not only on the soliton partition.

## 3. Exact hook-sector component count

Put

\[
 n=2m+1,qquad
 \lambda=(h,1^b),qquad b=m-h,qquad h\ge3.
\tag{3.1}
\]

Every component in this sector is wholly selected by Theorem 2.1.  The
sector has distinct soliton sizes `1,h`, multiplicities `b,1`, and vacancy
numbers

\[
                         q=2h-1,qquad 1.
\tag{3.2}

For an internal symmetry `gamma | gcd(b,q)`, the exact period matrix is

\[
 F_\gamma=
 \begin{pmatrix}
 (n-2)/\gamma&2\\
 2b/\gamma&2h+1
 \end{pmatrix},
 \qquad
 \det F_\gamma={nq\over\gamma}.
\tag{3.3}

PBBS translates by `(1,h)^T`.  Replacing the first column of `F_gamma`
by this vector gives determinant

\[
 \det\begin{pmatrix}1&2\\h&2h+1\end{pmatrix}=1.
\tag{3.4}

The Cramer order formula therefore gives period `nq/gamma`, equal to the
entire torus size.  Every action torus in the hook sector is one PBBS
cycle.

Let

\[
 L_\gamma(b,q)=
 \sum_{\gamma\mid\beta\mid\gcd(b,q)}
 \mu(\beta/\gamma)
 \binom{(q+b)/\beta-1}{b/\beta-1}.
\tag{3.5}
\]

The exact number of wholly selected PBBS components in this one sector is
therefore

\[
 \boxed{
 c_{m,h}^{hook}
 =\sum_{\gamma\mid\gcd(b,2h-1)}
 {\gamma\over b}
 L_\gamma(b,2h-1).}
\tag{3.6}

For `b=0`, the single-soliton sector consists of its familiar one minimum
cycle and is handled separately.

Two checks are immediate:

\[
 c_{m,m-1}^{hook}=1,
 \qquad
 c_{m,m-2}^{hook}=m-2.
\tag{3.7}

The first is the two-soliton component, and the second is the
`(m-2,1,1)` family encountered by the promotion connector.

## 4. Exponentially many wholly selected components

Take `m=3t`, `h=t`, and `b=2t`, with `t>=3`.  Then

\[
                         \gcd(b,2h-1)=\gcd(2t,2t-1)=1.
\]

Equation (3.6) reduces to the exact count

\[
 \boxed{
 c_{3t,t}^{hook}
 ={1\over2t}\binom{4t-2}{2t-1}.}
\tag{4.1}

The central-binomial estimate gives

\[
 c_{3t,t}^{hook}=\exp(\Omega(t))=\exp(\Omega(m)).
\tag{4.2}

All of these components are wholly contained in every max-height q1
section.  Hence:

### Corollary 4.1

The number of wholly max-height-selected PBBS components is not `O(1)`,
nor polynomial in `m`; it is exponential on the subsequence `m=3t`.

Consequently a bounded list of exceptional-cycle patches cannot establish
the graphic q1 gate for the canonical PBBS section.  Any successful PBBS
repair must use a genuinely global quotient construction (for example a
loose connector forest), or abandon the fixed max-height section on a
macroscopic family of occurrences.

This conclusion does not obstruct an `O(1)` additive word bound: the
number of internal carrier surgeries may grow with `m` without adding word
positions.  It does rule out the proposed shortcut that only the
single-soliton and two-soliton cycles need repair.
