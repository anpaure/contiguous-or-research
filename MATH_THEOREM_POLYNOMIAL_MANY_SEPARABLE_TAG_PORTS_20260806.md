# Polynomially many separable tag ports

**Date:** 2026-08-06  
**Method:** Reed--Solomon graph codes and an explicit staged Johnson
geodesic; no computation or finite search  
**Status:** unconditional code and local connector theorem.  A linear-size
tag reservoir supports `R^c` port signatures whose unordered pair unions
are all distinct.  The middle of every pair connector is therefore
resource-separated by its tag trace.  Packing the constant-length boundary
stages and constructing one capacity-faithful typed cap remain separate.

## 1. A 2-separable constant-weight family

Fix an integer `d>=1`.  Let `q` be a prime power and choose
`2d+1` distinct evaluation points `E subset F_q`.  Put

\[
 \mathcal T=E\times\mathbb F_q.
\tag{1.1}
\]

For every polynomial `f in F_q[x]` of degree at most `d`, define

\[
 C_f=\{(x,f(x)):x\in E\}.
\tag{1.2}
\]

Then

\[
 |\mathcal T|=(2d+1)q,
 \qquad |C_f|=2d+1,
 \qquad |\{C_f\}|=q^{d+1}.
\tag{1.3}
\]

### Theorem 1.1 (unordered pair-union separation)

If

\[
                         C_f\cup C_g=C_u\cup C_v,
\tag{1.4}
\]

then the unordered polynomial pairs agree:

\[
                         \{f,g\}=\{u,v\}.
\tag{1.5}
\]

#### Proof

At every `x in E`, equation (1.4) gives equality of the unordered value
pairs

\[
 \{f(x),g(x)\}=\{u(x),v(x)\}.
\]

Therefore `f+g=u+v` on `2d+1` points.  These polynomials have degree at
most `d`, so they are identical.  Likewise `fg=uv`: both sides have degree
at most `2d` and agree at `2d+1` points.

Put `s=f+g=u+v` and `p=fg=uv`.  In the integral domain `F_q[x]`,

\[
 (f-u)(f-v)=f^2-sf+p=0.
\]

Hence `f=u` or `f=v`, and the equality of sums gives the other member.
\(\square\)

For every fixed `c`, choose `d+1>=c` and, by Bertrand's postulate, a prime
`q=Theta(R)` small enough that `(2d+1)q<=R/2`.  Then a tag reservoir using
at most half the coordinates supplies `Theta(R^{d+1})`, and hence at least
`R^c`, port codes of constant weight.

## 2. Coded ports

Let the ground set have size `2R-1` and contain `mathcal T`.  A rank-`R`
owner `A_f` is an `f`-port when

\[
                         A_f\cap\mathcal T
                          =\mathcal T\setminus C_f.
\tag{2.1}
\]

This leaves a linear non-tag shore because `|mathcal T|<=R/2`.

### Theorem 2.1 (pair-coded Johnson connector)

Let `A_f,A_g` be distinct coded ports.  Put

\[
 a=|C_f-C_g|=|C_g-C_f|\le2d+1.
\tag{2.2}
\]

If their Johnson distance `ell` satisfies `ell>=2a`, there is a shortest
path from `A_f` to `A_g` with the following form.

1. In its first `a` edges, delete all tags in `C_g-C_f` and insert `a`
   non-tags from `A_g-A_f`.
2. In the middle, exchange only non-tags.
3. In its last `a` edges, insert all tags in `C_f-C_g` and delete non-tags.

Every owner and lower facet strictly between stages 1 and 3 has tag trace

\[
                         \mathcal T-(C_f\cup C_g).
\tag{2.3}
\]

Hence the central resources of connectors belonging to distinct unordered
port pairs are disjoint.

#### Proof

The tag differences are forced members of the endpoint set differences.
After removing them, `ell-a>=a` non-tag differences remain on each shore,
so the first and final banks may be selected as stated.  Exchange every
endpoint difference exactly once.  The path has `ell` edges and is
therefore shortest.

After stage 1 all tags in both codewords are absent, and no tag is changed
again before stage 3.  This proves (2.3).  Theorem 1.1 recovers the
unordered pair `{f,g}` from that trace, giving resource separation. \(\square\)

The `O(d)` boundary owners/facets have partial tag traces rather than the
full pair-union trace.  Since `d` is fixed, this is an absolute number of
resources per connector, but their simultaneous packing is not a formal
consequence of Theorem 2.1.

## 3. PBBS relevance and exact scope

The rank-stratified upper-backup theorem can produce a polynomial number of
unoriented protected paths, much more than the `O(sqrt R)` one-tag reservoir
can name individually.  Theorem 1.1 supplies enough signatures for all of
them using only `O(R)` tags.  A prospective extension programme is:

1. extend each backup endpoint to a far coded port;
2. order the paths and join successive codes by Theorem 2.1;
3. use random constant-weight shells to avoid the polynomial old bank in
   the `O(1)` boundary stages; and
4. schedule the long non-tag portions by the two-sided residence aperture.

What is proved here is only the algebraic code and the central connector.
The following remain open:

1. a simultaneous low-exposure packing of all endpoint arms and partial-tag
   boundary stages;
2. compatibility with one directed owner/lower factor completion;
3. one literal antecedent across all joined paths;
4. a typed occurrence-cap router; and
5. control of the potentially non-polynomial number of unprotected cycles
   introduced by the factor extension theorem.

Thus the code removes the **number of available signatures** as an obstacle
for polynomial backup banks.  It does not by itself solve global PBBS
completion.

