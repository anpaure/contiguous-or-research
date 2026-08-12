# An exact prefix-context functor for capped MSW paths

This note proves the nontrivial context operation that is actually valid for
the boundary-transposition quotient.  It replaces the incorrect appeal to
plain left concatenation in the earlier boundary-connectivity draft.

Throughout, `bar(w)` is bitwise complement, while

\[
                    \mu(w)=\overline{\operatorname{rev}(w)}
\]

is the Dyck-word mirror.  For a middle-level word `z`, let `o(z)` be the
unique Dyck root whose MSW path contains `z`.

## 1. Two elementary path identities

For Dyck words `P,Q`, the MSW flip recursion gives

\[
 \rho(PQ)=\rho(P)\mathbin\Vert(|P|+\rho(Q)).             \tag{1.1}
\]

Consequently

\[
 P(PQ)=P(P)Q\ \mathbin\Vert\
       \overline P\bigl(P(Q)\setminus\{Q\}\bigr).       \tag{1.2}
\]

For a primitive root `1a0`, the same recursion says that its middle piece is

\[
 \{\,1\mu(q)1:q\in P(\mu(a))\,\}.                       \tag{1.3}
\]

The last member of this middle piece is `1 bar(a) 1`.

## 2. Terminal insertion

If a word ends in one bit, write `w^-` for the word obtained by deleting
that bit.

### Lemma 1 (terminal insertion)

Let `r,U` be Dyck words.  If `q in P(r)` ends in `1`, then

\[
 q^-\operatorname{rev}(U)1
 \in
 P\bigl(r^-\mu(U)0\bigr).                              \tag{2.1}
\]

### Proof

Write `r=AS`, where `S=1a0` is the last primitive component of `r`.
The last coordinate is still zero while the `A`-part is being flipped.
Thus every member of `P(r)` ending in one has the form

\[
                         \overline A q_S,
 \qquad q_S\in P(S),\quad q_S\text{ ending in }1.       \tag{2.2}
\]

Also

\[
 r^-\mu(U)0=A\bigl(S^-\mu(U)0\bigr),                   \tag{2.3}
\]

so (1.2) reduces the claim to the case that `r=S` is primitive.

Let `r=1a0`.  Apart from the final vertex, the members of `P(r)` ending in
one are

\[
                         q=1\mu(p)1,
 \qquad p\in P(\mu(a)).                                 \tag{2.4}
\]

Put

\[
                         r'=1a\mu(U)0.
\]

Its inner mirrored root is

\[
 \mu(a\mu(U))=U\mu(a).                                  \tag{2.5}
\]

By (1.2), after the `U`-part of `P(U mu(a))` has been flipped, that path
contains `bar(U) p`.  Mirroring it in (1.3) gives

\[
 1\mu(\overline U p)1
   =1\mu(p)\operatorname{rev}(U)1
   =q^-\operatorname{rev}(U)1,                          \tag{2.6}
\]

which is the desired vertex of `P(r')`.

The remaining possibility is the final vertex

\[
                         q=0\overline a1.
\]

Its image in (2.1) is

\[
 0\overline a\operatorname{rev}(U)1
   =\overline{1a\mu(U)0},                               \tag{2.7}
\]

the final vertex of `P(r')`.  This proves the primitive case, and (2.2)--
(2.3) restore the initial Dyck prefix `A`.  ∎

## 3. The root map

Let `U` be a nonempty Dyck word.  Write its last-primitive decomposition as

\[
                         U=V(1W0),                      \tag{3.1}
\]

where `V,W` are Dyck.  For `b in {0,1}`, define

\[
                    \theta_b(U):=V\,bW0.               \tag{3.2}
\]

Thus `theta_1(U)=U`; `theta_0(U)` is obtained by changing the opening bit
of the last primitive component of `U` from one to zero.

Every nonempty Dyck root `h` can be written uniquely as `h=1bR`.  Define

\[
                    \mathsf H_U(1bR):=11\theta_b(U)R.   \tag{3.3}
\]

This is again Dyck.  For `b=1`, a balanced word `U` has simply been inserted
at height two.  For `b=0`, the two leading up-steps successively pay for the
two down-steps displayed in `theta_0(U)=V0W0`.

### Theorem 2 (prefix-context path functor)

For every Dyck root `h` and every middle-level word `z`,

\[
          10z\in P(h)
 \quad\Longrightarrow\quad
          10\overline U z\in P(\mathsf H_U(h)).          \tag{3.4}
\]

In particular, the owner of `10 bar(U) z` depends only on the owner of
`10z`, not on the chosen vertex `z`:

\[
             o(10\overline U z)=\mathsf H_U(o(10z)).     \tag{3.5}
\]

### Proof

There are two cases.

**Case 1: `h=10R`.**  Here `R` is Dyck, and the explicit concatenation

\[
 P(10R)=(10R,11R,01R,01R_1,\ldots,01\overline R)
\]

shows that its only vertex beginning in `10` is `10R` itself.  Hence
`z=R`.

Write `U=V(1W0)` as in (3.1) and put

\[
                         K=11V0W0.
\]

The word `K` is primitive, with inner Dyck word `a=1V0W`.  Now

\[
 \mu(a)=\mu(W)\,1\mu(V)0.                              \tag{3.6}
\]

In the path `P(mu(a))`, first flip the whole `mu(W)` component and then
take the last middle vertex of `P(1mu(V)0)`.  This gives

\[
             p=\operatorname{rev}(W)\,1
               \operatorname{rev}(V)1\in P(\mu(a)).    \tag{3.7}
\]

Since

\[
                  \mu(p)=0\overline V0\overline W,
\]

the middle-piece formula (1.3) puts

\[
 1\mu(p)1=10\overline U\in P(K).                       \tag{3.8}
\]

Appending `R` by (1.2) yields

\[
       10\overline U R\in P(KR)
       =P(11\theta_0(U)R),                              \tag{3.9}
\]

which is (3.4).

**Case 2: `h=11R`.**  In the first-return decomposition write

\[
                         h=1a0v.
\]

Here `a` is nonempty.  Put `r=mu(a)`.  A vertex of `P(h)` beginning in
`10` lies in its middle piece, so for some `q in P(r)`,

\[
                         10z=1\mu(q)1v.                 \tag{3.10}
\]

The second bit in (3.10) is zero, hence `mu(q)` begins in zero and `q` ends
in one.  Write `mu(q)=0d`; then `z=d1v`.

Lemma 1 gives

\[
 q'=q^-\operatorname{rev}(U)1
       \in P(r'),
 \qquad
 r'=r^-\mu(U)0.                                        \tag{3.11}
\]

Write `r=p0`.  Then `a=mu(r)=1mu(p)`.  If `c=mu(p)`, the original root is

\[
                         h=11c0v=11R,                   \tag{3.12}
\]

where `R=c0v`, while

\[
 \mu(r')=\mu(p\mu(U)0)=1U\mu(p)=1Uc.                   \tag{3.13}
\]

Thus the root whose middle piece is controlled by `P(r')` is

\[
        1\mu(r')0v=11Uc0v=11UR=\mathsf H_U(h).          \tag{3.14}
\]

Finally, if `q=t1`, then `d=mu(t)` and

\[
 \mu(q')=\mu(t\operatorname{rev}(U)1)
          =0\overline U d.                              \tag{3.15}
\]

Therefore the corresponding middle vertex is

\[
 1\mu(q')1v=10\overline U d1v
             =10\overline U z,                          \tag{3.16}
\]

as required.  ∎

## 4. Exact preservation of capped connectivity

Let `Gamma^partial` be the quotient graph obtained by swapping the first two
coordinates.  A boundary edge from a capped root `10x` can be witnessed in
the form

\[
 01z\in P(10x),\qquad 10z\in P(h),\qquad z\in P(x).     \tag{4.1}
\]

### Corollary 3

If capped roots `10X={10x:x in X}` are connected in `Gamma^partial`, then
so are

\[
                         10UX=\{10Ux:x\in X\}           \tag{4.2}
\]

for every Dyck prefix `U`.

### Proof

The final part of `P(Ux)` is `bar(U) P(x)`.  Hence (4.1) becomes

\[
 01\overline U z\in P(10Ux).
\]

After swapping the first two coordinates, Theorem 2 places the resulting
word `10 bar(U) z` in the single path `P(H_U(h))`.  Thus every old capped
root--hub incidence maps to a new one, and a connected incidence
certificate remains connected.  ∎

Dyck-suffix appending is the easier companion operation:

\[
 o(10zV)=o(10z)V,                                      \tag{4.3}
\]

so a capped certificate also survives `x -> xV`.

## 5. What this does not prove

The remaining MNW context operation is

\[
                         x\longmapsto1\mu(x)0.           \tag{5.1}
\]

After capping and swapping, its relevant states are

\[
                         101\mu(z)1.                    \tag{5.2}
\]

Unlike (3.5), their owners are not constant on the fibres of `o(10z)`;
explicit fibres split into a growing number of paths.  Thus Theorem 2
settles the genuinely noncommuting **Dyck-prefix** operation, but it does
not settle mirror-wrapping.  A proof that complete MNW witness cycles stay
connected after (5.1), or a different proof of boundary connectivity, is
still required before the Catalan component hierarchy can be called
unconditional.
